<template>
  <div class="card-container">
    <div v-for="(subject,subid) in sub_data" class="card" style="width: 18rem;">
      <div class="card-body">
        <h5 class="card-title">{{ subject.title }}</h5>
        <ul style=" overflow-y:auto; height: 120px;" class="list-group list-group-flush">
          <li v-for="(chapter, chpid) in subject.chapters" class="list-group-item">{{ chapter.chapter }}</li>
        </ul>
        <a v-if="client === 'admin'" class="card-link" @click.prevent="delete_sub(subject.id)">Delete</a>
        <router-link class="card-link" :to="{ path: '/chapter',query:{title:subject.title,id:subject.id}}">Start -> </router-link>
      </div>
    </div>
  </div>
  <add_button v-if="client === 'admin'" @refresh="fetchlist"/>
</template>
<script>

import { mapActions, mapGetters } from 'vuex';
import add_button  from '@/components/add_button.vue';


export default {
  name: 'HomeView',
  components:{
    add_button
    
  },
  computed: {
    ...mapGetters(['sub_data','client'])
  },
  methods:{
    ...mapActions(['delete','fetchlist']),
    async delete_sub(subject_id){
      const payload={
        type:'Subject',
        id:subject_id
      };
      await this.delete(payload);
      this.fetchlist();
    }
  },
  mounted(){
    this.fetchlist();
  }
}
</script>
<style>
body {
  margin: 0;
  padding: 0;
}

.card-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(20rem, 1fr));
  gap: 1rem;
  padding-top: 5rem;
  margin-left: 60px;
  overflow-y: auto;
}

.card {
  margin: 1rem;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}

.card:hover {
  transform: scale(1);
}

.card-title {
  font-size: 1.20rem;
  font-weight: bold;
}

.card-link {
  color: #008bff;
  text-decoration: none;
}

.card-link:hover {
  text-decoration: underline;
}
</style>