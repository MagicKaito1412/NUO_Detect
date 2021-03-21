import Vue from 'vue';
import Router from 'vue-router';

const Login = () => import('../views/login/login');
const LoginHome = () => import('../views/login/home');
const MainContainer = () => import('../views/main-container/main-container');
const Home = () => import('../views/main-container/home');

Vue.use(Router);

const ROUTES = [
    {
        path: '/',
        redirect: '/login',
        component: Login,
        children: [
            {
                path: '/login',
                name: 'login',
                component: LoginHome,
            },
        ]
    },
    {
        path: '/home',
        redirect: '/home',
        component: MainContainer,
        children: [
            {
                path: 'home',
                name: 'home',
                component: Home,
            },
        ]
    },
]

const router = new Router({
    routes: ROUTES,
    scrollBehavior() {
        return {
            x: 0,
            y: 0
        }
    },
});

router.beforeEach((to, from, next) => {
    if (to.name && to.path) {
        next();
    }
},);

export default router