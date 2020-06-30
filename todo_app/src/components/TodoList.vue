<template>
  <b-container class="table-container">
    <!-- User Interface controls -->

    <b-row>
      <!-- 'Add new' button -->
      <b-col>
        <b-button
            @click="setModalSettings('Create new todo', 'Create')"
            variant="success"
            v-b-modal.modal-new-todo
            size="sm"
        >
          Add new
        </b-button>
      </b-col>

      <!-- Search element -->
      <b-col lg="6">
        <b-form-group
            label="Search"
            label-cols-sm="3"
            label-align-sm="right"
            label-size="sm"
            label-for="filterInput"
            class="mb-0"
        >
          <b-input-group size="sm">
            <b-form-input
                v-model="filter"
                type="search"
                id="filterInput"
                placeholder="Type to Search"
            ></b-form-input>
            <b-input-group-append>
              <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
            </b-input-group-append>
          </b-input-group>
        </b-form-group>
      </b-col>

      <!-- Filter element -->
      <b-col>
        <b-form-group
            label="Filter"
            label-cols-sm="6"
            label-cols-md="4"
            label-cols-lg="3"
            label-align-sm="right"
            label-size="sm"
            label-for="filterSelect"
            class="mb-6"
        >
          <b-form-select
              v-model="filterByDate"
              id="filterSelect"
              size="sm"
              :options="filterByDateOptions"
              @input="dateFiltering"
          ></b-form-select>
        </b-form-group>
      </b-col>
    </b-row>

    <b-table
        show-empty
        small
        striped
        stacked="md"
        :items="filteredTodoList"
        :fields="fields"
        :filter="filter"
        :filterIncludedFields="filterOn"
    >
      <template v-slot:cell(date)="dateRow">
        {{ new Date(dateRow.value).toLocaleDateString() }}
        {{ new Date(dateRow.value).toLocaleTimeString() }}
      </template>

      <template v-slot:cell(actions)="actionRow">
        <b-button @click="actionRow.toggleDetails" variant="info" size="sm" class="mr-1">
          Details
        </b-button>
        <b-button @click="onUpdate(actionRow.item)" variant="outline-primary" size="sm" class="mr-1">
          Update
        </b-button>
        <b-button @click="onDelete(actionRow.item)" variant="danger" size="sm" class="mr-1">
          Delete
        </b-button>
      </template>

      <template v-slot:row-details="row">
        <b-card>
          <p>{{ row.item.text }}</p>
        </b-card>
      </template>
    </b-table>

    <NewTodoModalForm
        :title="modalTitle"
        :btn-name="modalBtnName"
        :todo-item="updatedTodoItem"
    />

  </b-container>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex';
  import NewTodoModalForm from "@/components/NewTodoModalForm";

  export default {
    name: "TodoList",
    components: {
      NewTodoModalForm,
    },
    data() {
      return {
        fields: [
          {key: 'name', label: 'Name'},
          {key: 'date', label: 'Date', class: 'text-center'},
          {key: 'actions', label: '', class: 'text-right'},
        ],

        filterByDate: 'all',
        filterByDateOptions: [
          'last day', 'last week', 'last month', 'all'
        ],

        filter: null,
        filterOn: ['name'],

        modalTitle: '',
        modalBtnName: '',
        updatedTodoItem: null,
      }
    },
    computed: mapGetters([
      'todoList', 'isTodoList', 'filteredTodoList',
      'todoListErrorStatus', 'todoListErrorMsg'
    ]),
    mounted() {
      this.fetchTodoList();
    },
    methods: {
      ...mapActions([
        'createTodo', 'fetchTodoList','updateTodo',
        'deleteTodo', 'filterTodoList'
      ]),

      onUpdate(todoItem) {
        this.setModalSettings(
          'Update todo', 'Update', todoItem
        )
        this.$bvModal.show('modal-new-todo');
      },

      onDelete(todoItem) {
        this.$bvModal.msgBoxConfirm('Please confirm that you want to delete this todo item.', {
          title: 'Please Confirm',
          size: 'sm',
          buttonSize: 'sm',
          okVariant: 'danger',
          okTitle: 'DELETE',
          cancelTitle: 'CANCEL',
          footerClass: 'p-2',
          hideHeaderClose: false,
          centered: true
        })
          .then(value => {
            if (value) {
              this.deleteTodo(todoItem);
            }
          })
      },

      setModalSettings(title, btnName, todoItem = null) {
        this.modalTitle = title;
        this.modalBtnName = btnName;
        this.updatedTodoItem = todoItem;
      },

      dateFiltering() {
        const filterDate = this.getFilterDate();

        if (filterDate) {
          const filteredTodoList = this.todoList.filter(todoItem => {
            const todoItemDate = new Date(todoItem.date);
            return todoItemDate >= filterDate && todoItemDate <= new Date();
          });

          this.filterTodoList(filteredTodoList)
        } else {
          this.filterTodoList(this.todoList)
        }
      },

      getFilterDate() {
        let filterDate = null;

        switch (this.filterByDate) {
          case 'last day':
            filterDate = new Date(new Date().setHours(-23));
            break;
          case 'last week':
            filterDate = new Date(new Date().setHours(-167));
            break;
          case 'last month':
            filterDate = new Date(new Date().setMonth(new Date().getMonth() - 1));
            break;
        }

        if (filterDate) {
           filterDate = new Date(filterDate.setHours(0, 0, 0, 0));
        }

        return filterDate;
      },
    },
  }
</script>

<style scoped>
  .table-container {
    margin-top: 25px;
    max-width: 750px;
  }
</style>