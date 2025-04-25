<template>
    <form>
        <div class="input-group mb-3">
            <select v-model="subject_id" class="form-select" id="inputGroupSelect02">
                <option selected>Choose...</option>
                <option :key="subject.id" :value="subject.id" v-for="subject in sub_data"value="0">{{subject.title}}</option>
            </select>
            <label class="input-group-text" for="inputGroupSelect02">Options</label>
        </div>
        <div class="input-group mb-3">
            <span class="input-group-text" id="inputGroup-sizing-default">Title</span>
            <input v-model="chapter" type="text" class="form-control" aria-label="Sizing example input"
                aria-describedby="inputGroup-sizing-default">
        </div>
        <button @click.prevent="add_sub" type="submit" class="btn btn-primary">Submit</button>
    </form>
</template>
<script>
import { mapGetters, mapActions } from 'vuex';
export default {
    data() {
        return {
            subject_id: "",
            chapter: ""
        }

    },
    computed :{
        ...mapGetters(['sub_data'])
    }
    , methods: {
        ...mapActions(['add', 'fetchlist']),
        async add_sub() {
            const payload = {
                type: 'Chapter',
                subject_id: this.subject_id,
                chapter: this.chapter
            };
            await this.add(payload);
            this.fetchlist();
            this.resetform();
            this.$emit('refresh');
        },
        resetform(){
            this.chapter=null;
        },
        
    }
}
</script>