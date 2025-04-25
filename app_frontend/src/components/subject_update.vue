<template>
    <form>
        <div class="input-group mb-3">
            <select v-model="subject_update_id" class="form-select" id="inputGroupSelect02" @change="populateFields">
                <option selected disabled>Choose...</option>
                <option :key="subject.id" :value="subject.id" v-for="subject in sub_data">
                    {{ subject.title }}
                </option>
            </select>
            <label class="input-group-text" for="inputGroupSelect02">Subjects</label>
        </div>
        <div class="input-group mb-3">
            <span class="input-group-text" id="inputGroup-sizing-default">Title</span>
            <input v-model="title" type="text" class="form-control" aria-label="Sizing example input"
                aria-describedby="inputGroup-sizing-default">
        </div>
        <div class="input-group mb-3">
            <span class="input-group-text" id="inputGroup-sizing-default">Description</span>
            <input v-model="description" type="text" class="form-control" aria-label="Sizing example input"
                aria-describedby="inputGroup-sizing-default">
        </div>
        <button @click.prevent="updateSubject" type="submit" class="btn btn-primary">Submit</button>
    </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
    data() {
        return {
            subject_update_id: null, 
            title: "", 
            description: "" 
        };
    },
    computed: {
        ...mapGetters(['sub_data'])
    },
    methods: {
        ...mapActions(['update', 'fetchlist']), 

        populateFields() {
            const selectedSubject = this.sub_data.find(subject => subject.id === this.subject_update_id);
            if (selectedSubject) {
                this.title = selectedSubject.title || ""; 
                this.description = selectedSubject.description || ""; 
            }
        },

        async updateSubject() {
            if (!this.subject_update_id) {
                alert("Please select a subject to update.");
                return;
            }

            const payload = {
                type: 'Subject',
                id: this.subject_update_id,
                title: this.title || undefined, 
                description: this.description || undefined 
            };
            console.log(payload)
            await this.update(payload);

            await this.fetchlist();
            this.resetForm();
            this.$emit('refresh');
        },

        resetForm() {
            this.subject_update_id = null;
            this.title = "";
            this.description = "";
        }
    }
};
</script>