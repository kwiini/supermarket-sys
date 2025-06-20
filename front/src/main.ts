import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'
import { createRouter, createWebHistory } from 'vue-router'
import 'element-plus/dist/index.css'
import ElementPlus from 'element-plus'
import 'virtual:uno.css'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: () => import('./views/Dashboard.vue') },
    { path: '/employee', component: () => import('./views/Employee.vue') },
    { path: '/suppliers', component: () => import('./views/Supplier.vue') },
    { path: '/members', component: () => import('./views/Member.vue') },
    { path: '/inventory', component: () => import('./views/Inventory.vue') },
    { path: '/sales', component: () => import('./views/Sale.vue') },
    { path: '/salesDetail', component: () => import('./views/SaleDetail.vue') },
    { path: '/products', component: () => import('./views/Product.vue') },
    { path: '/purchases', component: () => import('./views/Purchase.vue') },
  ],
});

createApp(App).use(ElementPlus).use(createPinia()).use(router).mount('#app');
