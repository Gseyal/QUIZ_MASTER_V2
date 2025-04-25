<template>
    <form>
        <!-- Subject Dropdown -->
        <div class="input-group mb-3">
            <select v-model="subject" class="form-select" id="inputGroupSelect02" @change="fetchChapters">
                <option selected disabled>Choose Subject...</option>
                <option :key="subject.id" :value="subject.id" v-for="subject in sub_data">{{ subject.title }}</option>
            </select>
            <label class="input-group-text" for="inputGroupSelect02">Subjects</label>
        </div>

        <!-- Chapter Dropdown -->
        <div class="input-group mb-3">
            <select v-model="chapter_id" :disabled="!subject" class="form-select" id="inputGroupSelect02"
                @change="fetchQuestionsFromBackend">
                <option selected disabled>Choose Chapter...</option>
                <option :key="chapter.id" :value="chapter.id" v-for="chapter in getChapters">{{ chapter.chapter }}
                </option>
            </select>
            <label class="input-group-text" for="inputGroupSelect02">Chapters</label>
        </div>

        <!-- Question Dropdown -->
        <div class="input-group mb-3">
            <select v-model="question_id" :disabled="!chapter_id" class="form-select" id="inputGroupSelect02"
                @change="populateFields">
                <option selected disabled>Choose Question...</option>
                <option :key="question.id" :value="question.id" v-for="question in questions">{{ question.question }}
                </option>
            </select>
            <label class="input-group-text" for="inputGroupSelect02">Questions</label>
        </div>

        <!-- Question Text Input -->
        <div class="input-group mb-3">
            <span class="input-group-text" id="inputGroup-sizing-default">Question</span>
            <input v-model="question" type="text" class="form-control" aria-label="Sizing example input"
                aria-describedby="inputGroup-sizing-default">
        </div>

        <!-- Options Input -->
        <div class="input-group mb-3">
            <div class="container text-center">
                <div class="row row-cols-2">
                    <div class="col"><input v-model="option1" placeholder="A." type="text" class="form-control"></div>
                    <div class="col"><input v-model="option2" placeholder="B." type="text" class="form-control"></div>
                    <div class="col"><input v-model="option3" placeholder="C." type="text" class="form-control"></div>
                    <div class="col"><input v-model="option4" placeholder="D." type="text" class="form-control"></div>
                </div>
            </div>
        </div>

        <!-- Correct Option Input -->
        <div class="input-group mb-3">
            <span class="input-group-text" id="inputGroup-sizing-default">Correct Option</span>
            <div class="col"><input v-model="correct" type="text" class="form-control"></div>
        </div>

        <!-- Submit Button -->
        <button @click.prevent="updateQuestion" type="submit" class="btn btn-primary">Submit</button>
    </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
    data() {
        return {
            subject: null, 
            chapter_id: null, 
            question_id: null, 
            question: "", 
            option1: "", 
            option2: "", 
            option3: "", 
            option4: "", 
            correct: "", 
        };
    },
    computed: {
        ...mapGetters(['sub_data', 'questions']),
        getChapters() {
            if (Array.isArray(this.sub_data) && this.subject) {
                const selectedSubject = this.sub_data.find(sub => sub.id === this.subject);
                return selectedSubject ? selectedSubject.chapters : [];
            }
            return [];
        }
    },
    methods: {
        ...mapActions(['update', 'fetchlist', 'fetchquestions']), 
        async fetchQuestionsFromBackend() {
            if (!this.chapter_id) {
                this.questions = [];
                return;
            }
            const payload = {

                chapter: this.chapter_id
            };
            await this.fetchquestions(payload);
        },
        populateFields() {
            const selectedQuestion = this.questions.find(question => question.id === this.question_id);
            if (selectedQuestion) {
                this.question = selectedQuestion.question || ""; 
                this.option1 = selectedQuestion.options[0] || ""; 
                this.option2 = selectedQuestion.options[1] || ""; 
                this.option3 = selectedQuestion.options[2] || ""; 
                this.option4 = selectedQuestion.options[3] || ""; 
                this.correct = selectedQuestion.correct || ""; 
            }
        },
        async updateQuestion() {
            if (!this.question_id) {
                alert("Please select a question to update.");
                return;
            }

            
            const payload = {
                type: 'Question',
                id: this.question_id,
                chapter_id: this.chapter_id,
                question: this.question || undefined,
                options: [this.option1, this.option2, this.option3, this.option4],
                correct: this.correct || undefined
            };

            
            await this.update(payload);

            
            await this.fetchlist();
            this.resetForm();
            this.$emit('refresh');
        },
        resetForm() {
            this.subject = null;
            this.chapter_id = null;
            this.question_id = null;
            this.question = "";
            this.option1 = "";
            this.option2 = "";
            this.option3 = "";
            this.option4 = "";
            this.correct = "";
            this.questions = [];
        }
    }
};
</script>