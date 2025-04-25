<template>
    <form>
        <!-- Subject Dropdown -->
        <div class="input-group mb-3">
            <select v-model="subject" class="form-select" id="inputGroupSelect02">
                <option selected disabled>Choose...</option>
                <option :key="subject.id" :value="subject.id" v-for="subject in sub_data">{{ subject.title }}</option>
            </select>
            <label class="input-group-text" for="inputGroupSelect02">Subjects</label>
        </div>

        <!-- Chapter Dropdown -->
        <div class="input-group mb-3">
            <select v-model="chapter_id" :disabled="!subject" class="form-select" id="inputGroupSelect02">
                <option selected disabled>Choose...</option>
                <option :key="chapter.id" :value="chapter.id" v-for="chapter in getChapters">{{ chapter.chapter }}</option>
            </select>
            <label class="input-group-text" for="inputGroupSelect02">Chapters</label>
        </div>

        <!-- Chapter Title Input -->
        <div class="input-group mb-3">
            <span class="input-group-text" id="inputGroup-sizing-default">Title</span>
            <input v-model="chapter" type="text" class="form-control" aria-label="Sizing example input"
                aria-describedby="inputGroup-sizing-default">
        </div>

        <!-- Submit Button -->
        <button @click.prevent="updateChapter" type="submit" class="btn btn-primary">Submit</button>
    </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
    data() {
        return {
            subject: "", 
            chapter_id: "", 
            chapter: "" 
        };
    },
    computed: {
        ...mapGetters(['sub_data']),
        getChapters() {
            if (Array.isArray(this.sub_data) && this.subject) {
                const selectedSubject = this.sub_data.find(sub => sub.id === this.subject);
                return selectedSubject ? selectedSubject.chapters : [];
            }
            return [];
        }
    },
    methods: {
        ...mapActions(['update', 'fetchlist']),
        async updateChapter() {
            
            if (!this.subject || !this.chapter_id || !this.chapter) {
                alert("Please fill all fields before submitting.");
                return;
            }
            const payload = {
                type: 'Chapter',
                subject_id: this.subject,
                chapter_id: this.chapter_id,
                chapter: this.chapter
            };
            await this.update(payload);
            this.fetchlist();
            this.resetForm();
            this.$emit('refresh');
        },
        resetForm() {
            this.subject = "";
            this.chapter_id = "";
            this.chapter = "";
        }
    }
};
</script>