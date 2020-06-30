<template>
  <div>
    <b-modal
        id="modal-sign-in"
        scrollable
        title="Sign In Form"
        @hidden="resetFormValues"
        @cancel="resetFormValues"
        @ok="onOk"
    >
      <b-form @submit.stop.prevent="handleSubmit">
        <b-form-group
            id="input-group-1"
            label="Email:"
            label-for="input-1"
        >
          <b-form-input
            id="input-1"
            v-model="$v.form.email.$model"
            :state="validateState('email')"
            aria-describedby="input-live-feedback"
            placeholder="Enter email"
            trim
          ></b-form-input>

          <!-- This will only be shown if the preceding input has an invalid state -->
          <b-form-invalid-feedback id="input-live-feedback">
            This filed is a required and must be a valid email address.
          </b-form-invalid-feedback>
        </b-form-group>

        <b-form-group
            id="input-group-2"
            label="Password:"
            label-for="input-2"
        >
          <b-form-input
              id="input-2"
              v-model="$v.form.password.$model"
              :state="validateState('password')"
              type="password"
              placeholder="Enter password"
          ></b-form-input>
        </b-form-group>
      </b-form>

      <template v-slot:modal-footer="{ ok, cancel }">
        <!-- Emulate built in modal footer ok and cancel button actions -->
        <b-button @click="cancel()">
          Cancel
        </b-button>
        <b-button variant="success" @click="ok()">
          Sign In
        </b-button>
      </template>

    </b-modal>
  </div>
</template>

<script>
  import { validationMixin } from "vuelidate";
  import { required, email } from "vuelidate/lib/validators";
  import { mapActions } from 'vuex';

  export default {
    name: "SignInModalForm",
    mixins: [validationMixin],
    data() {
      return {
        form: {
          email: '',
          password: '',
        },
        show: true,
      }
    },
    validations: {
      form: {
        email: {
          required,
          email,
        },
        password: {
          required,
        },
      },
    },
    methods: {
      ...mapActions(['signIn']),

      onOk(bvModalEvt) {
        bvModalEvt.preventDefault();
        this.handleSubmit();
      },

      handleSubmit() {
        this.$v.$touch();

        if (!this.isFieldsInvalid()) {
          this.signIn(this.form);
        }

        this.$nextTick(() => {
          this.$bvModal.hide('modal-sign-in')
        });
      },

      isFieldsInvalid() {
        return Object.keys(this.form).some(key => this.$v.form[key].$invalid)
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
    },
  }
</script>

<style scoped>

</style>