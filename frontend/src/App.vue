<template>
  <div id="inside-app">
    <header>
      <v-container fluid class="hero-section" fill-height>
        <v-row justify="center" align="center">
          <v-col class="text-center">
            <h1>Agent Bourne</h1>
            <p>Your go-to platform for amazing content.</p>
          </v-col>
        </v-row>
      </v-container>
    </header>

    <main>
      <router-view></router-view> <!-- This renders the current route's component -->
    </main>

    <footer>
      <!-- Your footer content -->
      <p>&copy; Agent Bourne</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      title: 'Welcome to Agent Bourne'
    }
  }
  // Additional component options can be defined here
}
</script>

<style>
/* Global styles for the entire application */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

#inside-app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

header {
  background-color: #333;
  color: white;
  padding: 10px;
}

main {
  flex: 1; /* Takes remaining space */
  padding: 20px;
}

footer {
  background-color: #333;
  color: white;
  text-align: center;
  padding: 10px;
}
</style>
