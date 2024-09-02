<template>
  <v-container>
    <v-row>
      <v-col>
        <div v-if="loading">Loading...</div>
        <div v-if="error">Error: {{ error.message }}</div>
        <div v-if="result">
          <ul v-if="result && result.sampleUserDetail">
            <li>
              {{ result.sampleUserDetail.id }} {{ result.sampleUserDetail.email }}
            </li>
          </ul>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
// import { watch } from 'vue';
import { useQuery } from '@vue/apollo-composable';
import { SAMPLE_USER_DETAIL } from '@/queries/testConnectionQuery';


const { result, loading, error } = useQuery(SAMPLE_USER_DETAIL);

// watch(() => {
//   console.log(result.value)
// });

</script>