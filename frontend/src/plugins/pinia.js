import { createPinia } from 'pinia';
import piniaPluginPersistedState from "pinia-plugin-persistedstate";

const pinia = createPinia();

// Please keep in mind that data stored in sessionStorage is not private and you should be careful with storing sensitive information there.
pinia.use(piniaPluginPersistedState);

export default pinia;
