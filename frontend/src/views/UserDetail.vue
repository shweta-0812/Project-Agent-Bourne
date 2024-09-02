<template>
  <v-container>
    <v-row>
      <v-col>
        <p>Welcome, {{ userDetailStore.name }}!</p>

<!--        <div v-if="userDetailStore.isAuthenticatedUser">-->
<!--        </div>-->
<!--        <div v-else>-->
<!--        </div>-->
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { userDetail } from '@/store';
const userDetailStore = userDetail();

</script>