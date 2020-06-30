<template>
  <b-modal
      id="modal-new-todo"
      scrollable
      :title="title"
      @hidden="resetFormValues"
      @cancel="resetFormValues"
      @ok="onOk"
      @shown="setUpdatedTodoItem"
  >
    <b-form @submit.stop.prevent="handleSubmit">
      <!-- Name filed -->
      <b-form-group
          id="name-input-group"
          label="Name:"
          label-for="name-input"
      >
        <b-form-input
            id="name-input"
            v-model="$v.form.name.$model"
            :state="validateState('name')"
            aria-describedby="input-live-feedback"
            placeholder="Enter name"
        ></b-form-input>

        <!-- This will only be shown if the preceding input has an invalid state -->
        <b-form-invalid-feedback id="input-live-feedback">
          This filed is required and must be no more than
          {{ $v.form.name.$params.maxLength.max }} characters.
        </b-form-invalid-feedback>

      </b-form-group>

      <!-- Text filed -->
      <b-form-group
          id="input-group-2"
          label="Text:"
          label-for="input-2"
      >
        <b-form-textarea
            id="input-2"
            v-model="$v.form.text.$model"
            :state="validateState('text')"
            aria-describedby="input-live-feedback"
            placeholder="Enter text"
            rows="4"
        ></b-form-textarea>

        <!-- This will only be shown if the preceding input has an invalid state -->
        <b-form-invalid-feedback id="input-live-feedback">
          This filed must be no more than
          {{ $v.form.text.$params.maxLength.max }} characters.
        </b-form-invalid-feedback>
      </b-form-group>

      <!-- Date filed -->
      <b-form-group
          id="input-group-3"
          label="Date:"
          label-for="input-3"
      >
        <b-form-datepicker
            v-model="$v.form.date.$model"
            :min="new Date()"
            locale="en"
            :state="validateState('date')"
            aria-describedby="input-live-feedback"
        ></b-form-datepicker>

        <!-- This will only be shown if the preceding input has an invalid state -->
        <b-form-invalid-feedback id="input-live-feedback">
          This filed is required.
        </b-form-invalid-feedback>
      </b-form-group>

      <!-- Time filed -->
      <b-form-group
          id="input-group-4"
          label="Time:"
          label-for="input-4"
      >
        <b-form-timepicker
            v-model="$v.form.time.$model"
            :state="validateState('time')"
            aria-describedby="input-live-feedback"
        ></b-form-timepicker>

        <!-- This will only be shown if the preceding input has an invalid state -->
        <b-form-invalid-feedback id="input-live-feedback">
          This filed is required.
        </b-form-invalid-feedback>
      </b-form-group>
    </b-form>

    <template v-slot:modal-footer="{ ok, cancel }">
      <!-- Emulate built in modal footer ok and cancel button actions -->
      <b-button @click="cancel()">
        Cancel
      </b-button>
      <b-button variant="success" @click="ok()">
        {{ btnName }}
      </b-button>
    </template>

  </b-modal>
</template>

<script>
  import {mapActions} from 'vuex';
  import {validationMixin} from "vuelidate";
  import {maxLength, required} from "vuelidate/lib/validators";

  export default {
    name: "NewTodoModalForm",
    mixins: [validationMixin],
    props: ['title', 'btnName', 'todoItem'],
    data() {
      return {
        form: {
          name: '',
          text: '',
          date: '',
          time: '',
        },
      }
    },
    validations: {
      form: {
        name: {
          required,
          maxLength: maxLength(64),
        },
        text: {
          maxLength: maxLength(512),
        },
        date: {
          required,
        },
        time: {
          required,
        },
      },
    },
    methods: {
      ...mapActions(['createTodo', 'updateTodo']),

      onOk(bvModalEvt) {
        bvModalEvt.preventDefault();
        this.handleSubmit();
      },

      handleSubmit() {
        this.$v.$touch();

        if (!this.isFieldsInvalid()) {
          switch (this.btnName) {
            case 'Create':
              this.createTodo(this.getValidForm())
              break;
            case 'Update':
              this.updateTodo({
                data: this.form,
                todoId: this.todoItem.pk,
              })
              break;
          }

          this.$nextTick(() => {
            this.$bvModal.hide('modal-new-todo')
          });
        }
      },

      isFieldsInvalid() {
        return Object.keys(this.form).some(key => this.$v.form[key].$invalid)
      },

      getValidForm() {
        let validForm = Object.assign({}, this.form);
        validForm.date = new Date(`${this.form.date} ${this.form.time}`);
        delete validForm.time;

        return validForm
      },

      resetFormValues() {
        Object.keys(this.form).forEach(key => {
          if (this.form[key]) {
            this.form[key] = '';
          }

          this.$nextTick(() => {
            this.$v.$reset();
          });
        });
      },

      validateState(key) {
        const { $dirty, $error } = this.$v.form[key];
        return $dirty ? !$error : null;
      },

      setUpdatedTodoItem() {
        if (this.todoItem) {
          this.form.name = this.todoItem.name;
          this.form.text = this.todoItem.text;
          this.form.date = this.todoItem.date;
          this.form.time = new Date(this.todoItem.date).toLocaleTimeString();
        }
      },
    },
  }
</script>

<style scoped>

</style>