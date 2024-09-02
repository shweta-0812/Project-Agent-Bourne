<template>
  <!-- Features Section -->
  <v-container fluid class="features-section">
    <v-row justify="center" align="center">
      <v-col class="text-center">
<!--          <v-card-title class="headline">Login</v-card-title>-->
          <v-card-text>
            <v-btn color="primary" @click="loginWithGoogle">Login with Google</v-btn>
          </v-card-text>
      </v-col>
<!--      <v-col cols="12" md="6" class="text-center">-->
<!--        <v-icon large>mdi-heart</v-icon>-->
<!--        <h3>Login</h3>-->
<!--        <v-btn :to="{ name: 'Login' }" link>-->
<!--          Go to Login Page-->
<!--        </v-btn>-->
<!--      </v-col>-->
    </v-row>
  </v-container>
</template>

<script setup>
import { onMounted } from 'vue';
import { generateSecureRandomString } from '@/utils';

onMounted( () => {
});

function loginWithGoogle() {
    const stateToken = (generateSecureRandomString(16));
    const GOOGLE_CLIENT_ID = import.meta.env.VITE_GOOGLE_CLIENT_ID;

    let redirectURI = `${window.location.origin}/auth/google/callback`

    if (import.meta.env.DEV) { //returns a boolean flag for which env it is using
      redirectURI = `http://localhost:5173/auth/google/callback`;
    }

    // set URL for redirecting to Google
    const googleAuthUrl = `${import.meta.env.VITE_GOOGLE_AUTH_URL}?client_id=${GOOGLE_CLIENT_ID}&redirect_uri=${redirectURI}&response_type=code&scope=profile email&state=${stateToken}`;
    window.location.href = googleAuthUrl;
  }



</script>

<style>
.fill-height {
  min-height: 100vh;
}
</style>