<template>
  <!-- Features Section -->
  <v-container fluid class="features-section">
    <v-row justify="center" align="center">
      <v-col cols="12" md="6" class="text-center">
        <p>Welcome, {{ userDetailStore.name }}!</p>
      </v-col>
      <v-col cols="12" md="6" class="text-center">
        <v-icon large>mdi-heart</v-icon>
        <v-btn :to="{ name: 'Logout' }" link>
          Logout
        </v-btn>
      </v-col>
    </v-row>
    <v-row justify="center" align="center">
      <v-col class="text-center">
        <v-textarea
            v-model="userInput"
            label="Type your task here..."
            rows="5"
            outlined
            class="input-textarea"
        ></v-textarea>
        <v-btn @click="sendData" color="primary" class="mt-4">
          Run Task
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { onMounted } from 'vue';
import { userDetail } from '@/store';
import { ref } from 'vue';
import {useQuery} from "@vue/apollo-composable";
import {SAMPLE_USER_DETAIL} from "@/queries/testConnectionQuery.js";

const userDetailStore = userDetail();
const userInput = ref(''); // To store the user's input

// function printState() {
//   console.log('Pinia Store State:');
//   // Iterate over the store state properties and print their values
//   Object.entries(userDetailStore.$state).forEach(([key, value]) => {
//     console.log(`${key}:`, value);
//   });
// }

onMounted(() => {
  // printState();
});


// const sendData = async () => {
//   try {
//     const response = await fetch('https://example.com/api/ask', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify({ question: userInput.value }),
//     });
//
//     const result = await response.json();
//     console.log('API Response:', result); // Handle the response as needed
//   } catch (error) {
//     console.error('Error sending data:', error);
//   }
// };

 const sendData = () => {
   const { result, loading, error } = useQuery(SAMPLE_USER_DETAIL);
 }
</script>
