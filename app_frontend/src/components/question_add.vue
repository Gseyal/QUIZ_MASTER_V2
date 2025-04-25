<!-- filepath: c:\Users\seyal\OneDrive\Desktop\QUIZ_MASTER_V2\app_frontend\src\components\question_add.vue -->
<template>
    <form>
        <div class="input-group mb-3">
            <select v-model="subject" class="form-select" id="inputGroupSelect02">
                <option selected disabled>Choose...</option>
                <option :key="subject.id" :value="subject.id" v-for="subject in sub_data">{{ subject.title }}</option>
            </select>
            <label class="input-group-text" for="inputGroupSelect02">Subjects</label>
        </div>
        <div class="input-group mb-3">
            <select v-model="chapter_id" :disabled="!subject" class="form-select" id="inputGroupSelect02">
                <option selected disabled>Choose...</option>
                <option :key="chapter.id" :value="chapter.id" v-for="chapter in getChapters">{{ chapter.chapter }}</option>
            </select>
            <label class="input-group-text" for="inputGroupSelect02">Chapters</label>
        </div>
        <div class="input-group mb-3">
            <span class="input-group-text" id="inputGroup-sizing-default">Question</span>
            <input v-model="question" type="text" class="form-control" aria-label="Sizing example input"
                aria-describedby="inputGroup-sizing-default">
        </div>
        <div class="input-group mb-3">
            <div class="container text-center">
                <div class="row row-cols-2">
                    <div class="col"><input v-model="option1" placeholder="A." type="text" class="form-control"
                            aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></div>
                    <div class="col"><input v-model="option2" placeholder="B." type="text" class="form-control"
                            aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></div>
                    <div class="col"><input v-model="option3" placeholder="C." type="text" class="form-control"
                            aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></div>
                    <div class="col"><input v-model="option4" placeholder="D." type="text" class="form-control"
                            aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default"></div>
                </div>
            </div>
        </div>
        <div class="input-group mb-3">
            <span class="input-group-text" id="inputGroup-sizing-default">Correct Option</span>
            <div class="col"><input v-model="correct" type="text" class="form-control" aria-label="Sizing example input"
                    aria-describedby="inputGroup-sizing-default"></div>
        </div>
        <button @click.prevent="add_question" type="submit" class="btn btn-primary">Submit</button>
    </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
    data() {
        return {
            subject: null,
            chapter_id: null,
            question: "",
            option1: "",
            option2: "",
            option3: "",
            option4: "",
            correct: ""
        }
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
        ...mapActions(['add', 'fetchlist']),
        async add_question() {
            const payload = {
                type: 'Question',
                chapter_id: this.chapter_id,
                question: this.question,
                options: [this.option1, this.option2, this.option3, this.option4],
                correct: this.correct
            };
            await this.add(payload);
            await this.fetchlist();
            this.resetForm();
            await this.$emit('refresh');
        },
        resetForm() {
            
            this.question = "";
            this.option1 = "";
            this.option2 = "";
            this.option3 = "";
            this.option4 = "";
            this.correct = "";
        }
    }
}
</script>