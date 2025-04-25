import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/store'
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
import '../node_modules/bootstrap/dist/js/bootstrap.bundle.min.js'

const app=createApp(App);
app.use(store);
app.use(router);
app.mount('#app');
