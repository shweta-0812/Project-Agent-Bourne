<template>
  <v-container class="d-flex justify-center align-center" fill-height>
    <v-row justify="center" align="center">
      <v-col class="text-center">
        <p>Processing...</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

import { getCookie, setInLocalStorage } from '@/utils';
import { userDetail } from '@/store';
import { JWT_TOKEN_KEY, CSRF_TOKEN_KEY } from '@/constants';

const userDetailStore = userDetail();
const router = useRouter();

async function googleCallback() {
  const csrfToken = getCookie(CSRF_TOKEN_KEY);
  const urlParams = new URLSearchParams(window.location.search);
  const code = urlParams.get('code');
  const state = urlParams.get('state');

  if (code && state) {
    try {
      const response = await fetch(import.meta.env.VITE_GOOGLE_AUTH_CALLBACK_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ code, state }),
      });

      // Check if the response is OK and has JSON content
      if (response.ok) {
        const data = await response.json();
        // Handle the response from your server
        // 1. store JWT in session storage
        setInLocalStorage(JWT_TOKEN_KEY, JSON.stringify(data.jwt_token));

        // 2. update user details in state ( stored in browser session storage )
        userDetailStore.$patch((state) => {
          state.user_id = data.user_id
          state.name = data.name
          state.email = data.email
          state.picture = data.picture
          state.isAdmin = false
        });

        // redirect
        router.push('/dashboard');
      } else {
        console.error('Error during authentication: Response not OK', response.status);
        // Handle non-OK response
        router.push('/login');
      }

    } catch (error) {
      console.error('Error during authentication', error);
    }
  }
}

onMounted(async () => {
  await googleCallback();
});
</script>

<style>
</style>
