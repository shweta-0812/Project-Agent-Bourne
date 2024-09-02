<template>
  <v-container></v-container>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { userDetail } from '@/store';

const router = useRouter();
const userDetailStore = userDetail();

function clearStorage() {
  // Clear session storage
  sessionStorage.clear();
  // Clear local storage
  localStorage.clear();
}

function resetStore() {
  userDetailStore.$reset();
}

function logoutUser() {
  clearStorage();
  resetStore();
  // Optionally, navigate to the login page
  router.push('/login');
}

onMounted( () => {
  logoutUser();
});

</script>