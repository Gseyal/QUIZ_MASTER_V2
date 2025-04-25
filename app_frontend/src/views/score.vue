<template>
    <div id="score_box">
        <div class="container text-center">
            <div class="row row-cols-4">
                <div class="col">Date</div>
                <div class="col">Subject</div>
                <div class="col">Chapter</div>
                <div class="col">Score</div>
            </div>
            <div v-for="(row,index) in score"  class="row row-cols-4">
                <div class="col">{{ row.date }}</div>
                <div class="col">{{ row.subject }}</div>
                <div class="col">{{ row.chapter }}</div>
                <div class="col">{{ row.score }}/{{ row.outof }}</div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters,mapActions } from 'vuex';
export default {
    computed:{
        ...mapGetters(['id','score'])
    },
    methods:{
        ...mapActions(['fetchscore']),
        async getscore(){
            const payload={
                user_id:this.id,
            };
            this.fetchscore(payload);
        }
    },
    mounted(){
        this.getscore();
    }
}
</script>
<style>
#score_box{
    padding-top:5rem;
    width: 100%;
}
</style>