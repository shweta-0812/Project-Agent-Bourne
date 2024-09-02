import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/AppHome.vue';
import Login from '@/views/AppLogin.vue';
import Test from '@/views/TestView.vue';
import TestConnection from '@/views/TestConnection.vue';
import Dashboard from '@/views/UserDashboard.vue';
import Callback from '@/views/GoogleCallback.vue';
import UserDetail from '@/views/UserDetail.vue';
import Logout from '@/views/AppLogout.vue';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/test',
        name: 'Test',
        component: Test
    },
    {
        path: '/auth/google/callback',
        name: 'Callback',
        component: Callback,
    },
    {
        path: '/test-connection',
        name: 'TestConnection',
        component: TestConnection,
        meta: { requiresAuth: true }
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: Dashboard,
        meta: { requiresAuth: true }
    },
    {
        path: '/logout',
        name: 'Logout',
        component: Logout,
        meta: { requiresAuth: true }
    },
    {
        path: '/me',
        name: 'Me',
        component: UserDetail,
        meta: { requiresAuth: true }
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes
});


// Add the router guard here
router.beforeEach((to, from, next) => {
    let isAuthenticated = false;

    const JWT = localStorage.getItem('JwtToken');
    if(JWT !== 'undefined' || JWT !== '' || JWT !== null){
         isAuthenticated = true;
    }

    // Check if the route requires authentication and if the user is not authenticated
    if (to.matched.some(record => record.meta.requiresAuth) && !isAuthenticated) {
        // Redirect to login page
        next({ name: 'Login' });
    } else {
            // Proceed to the next route
            next();
    }
});
export default router;
