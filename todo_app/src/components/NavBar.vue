<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="secondary">
      <b-navbar-brand href="#">TODO list</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown right>

<!--            <SignInModalForm/>-->
<!--            <SignUpModalForm/>-->

            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>User</em>
            </template>
<!--            <b-dropdown-item v-if="!isToken" v-b-modal.modal-sign-up>Sign Up</b-dropdown-item>-->
<!--            <b-dropdown-item v-if="!isToken" v-b-modal.modal-sign-in>Sign In</b-dropdown-item>-->

<!--            <b-dropdown-item v-if="isToken" @click="signOut">Sign Out</b-dropdown-item>-->
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
  // import SignInModalForm from './SignInModalForm.vue'
  // import SignUpModalForm from './SignUpModalForm.vue'
  // import { mapGetters, mapActions } from 'vuex';

  export default {
    name: "NavBar",
    components: {
      // SignInModalForm,
      // SignUpModalForm,
    },
    // computed: mapGetters(['isArtist', 'isToken', 'query']),
    // methods: mapActions(['signOut', 'filterAlbums', 'changeQuery']),
  }
</script>

<style scoped>
  .logo-link:hover,
  .logo-link:active,
  .logo-link {
    color: unset;
    text-decoration: unset;
  }

</style>