import Vue from 'vue';
import Router from 'vue-router';

const Login = () => import('../views/login/login');
const LoginHome = () => import('../views/login/home');
const MainContainer = () => import('../views/main-container/main-container');
const Home = () => import('../views/main-container/home');
const Doctors = () => import('../views/main-container/doctor/doctors');
const Doctor = () => import('../views/main-container/doctor/doctor');
const Patients = () => import('../views/main-container/patient/patients');
const Patient = () => import('../views/main-container/patient/patient');
const Ekg = () => import('../views/main-container/ekg/ekg');
const Statistics = () => import('../views/main-container/statistics');

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
        path: '/system',
        redirect: '/home',
        component: MainContainer,
        children: [
            {
                path: 'home',
                name: 'home',
                component: Home,
                children: [
                    {
                        path: 'doctors',
                        name: 'doctors',
                        component: Doctors,
                    }, {
                        path: 'doctor',
                        name: 'doctor',
                        component: Doctor,
                    }, {
                        path: 'patients',
                        name: 'patients',
                        component: Patients,
                    }, {
                        path: 'patient',
                        name: 'patient',
                        component: Patient,
                    }, {
                        path: 'ekg',
                        name: 'ekg',
                        component: Ekg,
                    }, {
                        path: 'statistics',
                        name: 'statistics',
                        component: Statistics,
                    },
                ]
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