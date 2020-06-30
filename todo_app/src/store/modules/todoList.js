'use strict';

export default {
  actions: {
    createTodo(ctx, data) {
      // fetch('http://httpstat.us/500') // test for 500 status
      fetch('/api/todo/', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
          'Content-type': 'application/json',
          'Authorization': localStorage.getItem('token'),
        },
      })
        .then(response => {
          if (response.status === 401) {
            localStorage.removeItem('token');
          }
          return response.json();
        })
        .then(newTodo => {
          ctx.commit('addNewTodoInTodoList', newTodo);
          ctx.commit('updateTodoErrorStatus', false);
        })
        .catch(error => {
          ctx.commit('updateTodoErrorMessage', error.message);
          ctx.commit('updateTodoErrorStatus', true);
        });
    },

    fetchTodoList(ctx) {
      // fetch('http://httpstat.us/500') // test for 500 status
      fetch('/api/todo/', {
        method: 'GET',
        headers: {
          'Content-type': 'application/json',
          'Authorization': localStorage.getItem('token'),
        }
      })
        .then(response => {
          switch (response.status) {
            case 401:
              localStorage.removeItem('token');
              throw new Error('unauthorized');
            case 200:
              return response.json();
            default:
              throw new Error(`${response.status}`);
          }
        })
        .then(todoList => {
          ctx.commit('updateTodoList', todoList);
          ctx.commit('updateTodoErrorStatus', false);
        })
        .catch(error => {
          ctx.commit('updateTodoErrorMessage', error.message);
          ctx.commit('updateTodoErrorStatus', true);
        });
    },

    updateTodo(ctx, payload) {
      // fetch('http://httpstat.us/500') // test for 500 status
      fetch(`/api/todo/${payload.todoId}/`, {
        method: 'PATCH',
        body: JSON.stringify(payload.data),
        headers: {
          'Content-type': 'application/json',
          'Authorization': localStorage.getItem('token'),
        },
      })
        .then(response => {
          if (response.status === 401) {
            localStorage.removeItem('token');
          }
          return response.json();
        })
        .then(updatedTodo => {
          ctx.commit('updateTodoInTodoList', updatedTodo);
          ctx.commit('updateTodoErrorStatus', false);
        })
        .catch(error => {
          ctx.commit('updateTodoErrorMessage', error.message);
          ctx.commit('updateTodoErrorStatus', true);
        });
    },

    deleteTodo(ctx, todoItem) {
      // fetch('http://httpstat.us/500') // test for 500 status
      fetch(`/api/todo/${todoItem.pk}/`, {
        method: 'DELETE',
        headers: {
          'Content-type': 'application/json',
          'Authorization': localStorage.getItem('token'),
        },
      })
        .then(response => {
          if (response.status === 401) {
            localStorage.removeItem('token');
          }
          if (response.status === 204) {
            ctx.commit('deleteTodoFromTodoList', todoItem);
            ctx.commit('updateTodoErrorStatus', false);
          }
        })
        .catch(error => {
          ctx.commit('updateTodoErrorMessage', error.message);
          ctx.commit('updateTodoErrorStatus', true);
        });
    },

    filterTodoList(ctx, filteredTodoList) {
      ctx.commit('updateFilteredTodoList', filteredTodoList);
    },
  },
  mutations: {
    updateTodoList(state, todoList) {
      state.todoList = todoList;
      state.filteredTodoList = todoList;
    },

    updateFilteredTodoList(state, filteredTodoList) {
      state.filteredTodoList = filteredTodoList;
    },

    deleteTodoFromTodoList(state, todoItem) {
      const currentIdx = state.todoList.indexOf(todoItem);
      state.todoList.splice(currentIdx, 1);
      state.filteredTodoList = state.todoList;
    },

    updateTodoInTodoList(state, todoObj) {
      const currentIdx = state.todoList.findIndex(
        todoItem => todoItem.pk === todoObj.pk
      );
      state.todoList[currentIdx] = todoObj;
      state.filteredTodoList = state.todoList;
    },

    addNewTodoInTodoList(state, todoItem) {
      state.todoList.unshift(todoItem);
      state.filteredTodoList = state.todoList;
    },

    updateTodoErrorStatus(state, errorStatus) {
      state.hasTodoListError = errorStatus;
    },

    updateTodoErrorMessage(state, errorMessage) {
      state.todoListErrorMessage = errorMessage;
    },
  },
  state: {
    todoList: [],
    filteredTodoList: [],
    hasTodoListError: false,
    todoListErrorMessage: '',
  },
  getters: {
    todoList(state) {
      return state.todoList;
    },

    filteredTodoList(state) {
      return state.filteredTodoList;
    },

    isTodoList(state) {
      return Boolean(Object.keys(state.todoList).length);
    },

    todoListErrorStatus(state) {
      return state.hasTodoListError;
    },

    todoListErrorMsg(state) {
      return state.todoListErrorMessage;
    },
  },
};