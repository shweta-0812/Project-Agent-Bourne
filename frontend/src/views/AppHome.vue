<template>
  <v-container></v-container>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { userDetail } from '@/store';

const router = useRouter();
const userDetailStore = userDetail();

function checkAndRoute() {
  let isAuthenticatedUser = false;
  isAuthenticatedUser =  userDetailStore.isAuthenticatedUser;

  if (!isAuthenticatedUser) {
      router.push('/login');
  } else {
    router.push('/dashboard');
  }
}

onMounted( () => {
  checkAndRoute();
});

</script>
