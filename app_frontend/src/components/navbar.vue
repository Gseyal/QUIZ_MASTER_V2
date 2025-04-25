<template>
    <nav id="nav" class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <router-link id="brand" class="navbar-brand" :to="{ path: '/' }">{{ name }}</router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item" style="width: fit-content;">
                        <router-link v-if="client === 'user'" class="nav-link" :to="{ path: '/score' }"
                            id="user_button2">Quiz</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link v-if="client==='user'" class="nav-link" :to="{ path: '/stat' }" id="admin_button3">Summary</router-link>
                        <router-link v-if="client==='admin'" class="nav-link" :to="{ path: '/admin_summary' }" id="admin_button3">Summary</router-link>
                    </li>
                    <button data-bs-toggle="modal" data-bs-target="#example2Modal" type="button" class="btn btn-outline-success"><svg xmlns="http://www.w3.org/2000/svg"
                            width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                            <path
                                d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0" />
                        </svg> Search</button>

                </ul>
                <div style='position: absolute; top:10px; right:10px;'>
                    <router-link @click.prevent="logout" v-if="status === 'Logout'" class="nav-link"
                        :to="{ path: '/' }">{{ status }}</router-link>
                    <router-link v-if="status === 'Login'" class="nav-link"
                        :to="{ path: '/login' }">{{ status }}</router-link>
                </div>
            </div>
        </div>
    </nav>
    <search_modal/>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import search_modal  from './search_modal.vue';

export default {
    components:{
        search_modal
    },
    data() {
        return {
            name: 'QuiZ master',
        }
    },
    computed: {
        ...mapGetters(['client', 'username', 'authenticated']),
        status() {
            return this.authenticated ? 'Logout' : 'Login'
        }

    },
    methods: {
        ...mapActions(['logout'])
    }
}
</script>
<style>
#nav {
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;

}

#brand {
    color: #00e600;
}
</style>