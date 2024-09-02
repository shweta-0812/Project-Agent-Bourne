import { createApp, h } from 'vue'
import App from '@/App.vue';
import router from '@/router'; // Vue Router
import vuetify from '@/plugins/vuetify'; // Vuetify setup
import pinia from '@/plugins/pinia';
import { useApollo } from '@/plugins/apollo';

import * as style from '@/style.css'; // eslint-disable-line no-unused-vars


// Create the Vue application instance
const app = createApp({
    setup() {
        useApollo()
    },
    render: () => h(App),
})

// Use plugins or setup tasks here (e.g., Vue Router, Vuetify)
app.use(pinia)
app.use(router)
app.use(vuetify)

// Mount the application to the #app element in public/index.html
app.mount('#app')