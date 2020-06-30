'use strict';

export default {
  actions: {
    getTokenFromLocalStorage(ctx) {
      const token = localStorage.getItem('token');
      if (token) {
        ctx.commit('updateToken', token);
      }
    },

    signUp(ctx, data) {
      fetch('/api/auth/users/' ,{
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
          'Content-type': 'application/json',
        }
      })
      .then(response => response.json())
      .then(user => {
        ctx.dispatch('signIn', {
          email: data.email,
          password: data.password,
        });
        ctx.commit('updateUser', user);
      })
      .catch(error => {
        ctx.commit('updateAuthErrorMessage', error.message);
        ctx.commit('updateAuthErrorStatus', true);
      });
    },

    signIn(ctx, data) {
      fetch('/api/auth/token/login/', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
          'Content-type': 'application/json',
        }
      })
        .then(response => response.json())
        .then(tokenObj => {
          const token = tokenObj['auth_token'];
          ctx.commit('updateToken', token);
          localStorage.setItem('token', token);
        })
        .catch(error => {
          ctx.commit('updateAuthErrorMessage', error.message);
          ctx.commit('updateAuthErrorStatus', true);
        });
    },

    signOut(ctx) {
      // fetch('http://httpstat.us/500') // тест на ошибку
      fetch('/api/auth/token/logout/', {
        method: 'POST',
        headers: {
          'Content-type': 'application/json',
          'Authorization': `Token ${localStorage.getItem('token')}`,
        },
      })
        .then(response => {
          if (response.status === 204) {
            localStorage.removeItem('token');
            ctx.commit('updateToken', '');
            ctx.commit('updateUser', {});
          }
          ctx.commit('updateAuthErrorStatus', false);
        })
        .catch(error => {
          ctx.commit('updateAuthErrorMessage', error.message);
          ctx.commit('updateAuthErrorStatus', true);
        });
    },
  },
  mutations: {
    updateToken(state, token) {
      state.token = token;
    },

    updateUser(state, user) {
      state.user = user;
    },

    updateAuthErrorStatus(state, errorStatus) {
      state.hasAuthError = errorStatus;
    },

    updateAuthErrorMessage(state, errorMessage) {
      state.authErrorMessage = errorMessage;
    },
  },
  state: {
    token: '',
    user: {},
    hasAuthError: false,
    authErrorMessage: '',
  },
  getters: {
    token(state) {
      return state.token;
    },

    isToken(state) {
      return Boolean(state.token);
    },

    user(state) {
      return state.user;
    },

    isUser(state) {
      return Boolean(Object.keys(state.user).length);
    },

    authErrorStatus(state) {
      return state.hasAuthError;
    },

    authErrorMsg(state) {
      return state.authErrorMessage;
    },
  },
};