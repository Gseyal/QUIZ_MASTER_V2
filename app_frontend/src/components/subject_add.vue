<template>
    <form >
        <div class="input-group mb-3">
            <span class="input-group-text" id="inputGroup-sizing-default">Title </span>
            <input  v-model="title" type="text" class="form-control" aria-label="Sizing example input"
                aria-describedby="inputGroup-sizing-default">
        </div>
        <div class="input-group mb-3">
            <span class="input-group-text" id="inputGroup-sizing-default">Description</span>
            <input  v-model="description" type="text" class="form-control" aria-label="Sizing example input"
                aria-describedby="inputGroup-sizing-default">
        </div>
        <button @click.prevent="add_sub" type="submit" class="btn btn-primary">Submit</button>
    </form>
</template>
<script>
import { mapGetters,mapActions } from 'vuex';
export default {
    data(){
        return {
            title:"",
            description:""
        }
        
    }
    ,methods:{
        ...mapActions(['add','fetchlist']),
        async add_sub(){
            const payload={
                type:'Subject',
                title:this.title,
                description:this.description
            };
            await this.add(payload);
            await this.fetchlist();
            await this.resetForm();
            await this.$emit('refresh');
            
        },
        resetForm() {
            this.title = "";
            this.description = "";
        },
        
    }
}
</script>