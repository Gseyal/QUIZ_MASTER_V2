import { createStore } from 'vuex';

const store = createStore({
    state: {
            sub_data: [],
            questions: [],
            token: null,
            username: null,
            client: null,
            authenticated: false,
            id:null,
            score:[],
            
    },
    mutations: {
        
        setData(state, sub_data) {
            state.sub_data = sub_data;
        },
        setscore(state, score) {
            state.score = score;
        },
        setquestion(state, questions) {
            state.questions = questions;
        },
        setToken(state, token) {
            state.token = token;
            state.authenticated = true;
        },
        setusername(state, username) {
            state.username = username;
        },
        setid(state, id) {
            state.id = id;
        },
        setclient(state, client) {
            state.client = client;
        },
        setlogout(state){
            state.token= null;
            state.username= null;
            state.client= null;
            state.authenticated= false;
            state.id=null;
        }
    },
    actions: {
        async update({commit},payload){
            try{
                console.log(payload)
                const response =await fetch("http://127.0.0.1:5000/update",{
                    method:'PUT',
                    headers: {
                        'Content-Type':'application/json'
                    },
                    body: JSON.stringify(payload)
                });
                alert("Updated!!")
            }catch(error){
                console.error(error)
                alert("Error Updating")
            }
        },
        async logout({commit}){
            commit('setlogout')
            alert("Logout")
            
        },
        async delete({commit},payload){
            try{
                const response =await fetch("http://127.0.0.1:5000/delete",{
                    method:'POST',
                    headers: {
                        'Content-Type':'application/json'
                    },
                    body: JSON.stringify(payload)
                });
                const data=await response.json();
                commit('setData',data)
                alert("data Deleted")

            }catch(error){
                console.error(error)
                alert("error in deleting")
            }
        },
        async add({commit},payload){
            try{
                const response =await fetch("http://127.0.0.1:5000/add_data",{
                    method:'POST',
                    headers: {
                        'Content-Type':'application/json'
                    },
                    body: JSON.stringify(payload)
                });
                const data=await response.json();
                commit('setData',data)
                alert("added")
            }catch(error){
                console.error(error)
            }
        },
        async getinfo({ commit }, payload) {
            try {
                const response = await fetch("http://127.0.0.1:5000/post", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                });
                const data = await response.json();
                commit('setToken', data.token);
                commit('setusername', data.name);
                commit('setclient', data.role);
                commit('setid', data.id);
                alert("Welcome"+":" +data.name)
            } catch (error) {
                console.error(error)
                alert("Check")
            }
        },
        async sendinfo({ commit }, payload) {
            try {
                const response = await fetch("http://127.0.0.1:5000/signup", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                });
                const data = await response.json();
                commit('setToken', data.token);
                commit('setusername', data.name);
                commit('setclient', data.role);
                commit('setid', data.id);
            } catch (error) {
                console.error(error)
            }
        },
        async fetchlist({ commit }) {
            try {
                const response = await fetch("http://127.0.0.1:5000/get_sub");
                const data = await response.json();
                commit('setData', data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        },
        async fetchquestions({ commit }, payload) {
            try {
                const response = await fetch("http://127.0.0.1:5000/get_question", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                });
                const data = await response.json();
                commit('setquestion', data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        },
        async fetchscore({ commit }, payload) {
            try {
                const response = await fetch("http://127.0.0.1:5000/get_score", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                });
                const data = await response.json();
                commit('setscore', data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        },
    },

    getters: {
        sub_data: state => state.sub_data,
        questions: state => state.questions,
        token: state => state.token,
        username: state => state.username,
        client: state => state.client,
        authenticated: state => state.authenticated,
        id: state => state.id,
        score: state => state.score,
    }
});

export default store;