<template>
    <div id="quiz_container">
        <!-- Timer Display -->
        <div v-if="client==='user'" id="timer" class="text-center mb-3">
            <h3>Time Remaining: {{ formattedTime }}</h3>
        </div>

        <form>
            <div id="question_box" v-for="(question, qIndex) in questions" class="mb-3">
                <label style="font-weight: bold; font-size: large;" for="exampleInputEmail1" class="form-label">
                    {{ question.question }}
                </label>
                <button v-if="client === 'admin'" @click.prevent="del_question(question.id)" class="btn btn-danger">
                    Delete
                </button>

                <div class="container text-center">
                    <div class="row row-cols-2">
                        <button
                            @click.prevent="selectoption(question.id, option)"
                            v-for="(option, oIndex) in question.options"
                            :class="[{ 'col': false }, { 'btn btn-primary': isSelected(question.id, option) }]">
                            {{ option }}
                        </button>
                    </div>
                </div>
            </div>
            <button type="submit" class="btn btn-primary" @click.prevent="sendanswers">Submit</button>
        </form>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
    data() {
        return {
            selection_list: {},
            subject: this.$route.query.subject || 'No Subject',
            chapter: this.$route.query.chapter || 'No Chapter',
            timer: 300, // Timer in seconds (e.g., 5 minutes = 300 seconds)
            timerInterval: null // Reference to the interval
        };
    },
    computed: {
        isSelected() {
            return (qIndex, oIndex) => {
                return this.selection_list[qIndex] === oIndex;
            };
        },
        ...mapGetters(['questions', 'id', 'client']),
        formattedTime() {
            // Format the timer as MM:SS
            const minutes = Math.floor(this.timer / 60);
            const seconds = this.timer % 60;
            return `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
        }
    },
    methods: {
        selectoption(qIndex, oIndex) {
            this.selection_list[qIndex] = oIndex;
        },
        ...mapActions(['fetchquestions', 'delete']),
        sendanswers() {
            this.selection_list.id = this.id;
            fetch("http://127.0.0.1:5000/score", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.selection_list)
            }).catch(error => {
                console.error('Error:', error);
            });
            this.$router.push({ path: '/score' });
        },
        async del_question(id) {
            const payload = {
                type: 'Question',
                id: id
            };
            await this.delete(payload);
            this.fetchQuestions();
        },
        fetchQuestions() {
            const payload = {
                chapter: this.chapter
            };
            this.fetchquestions(payload);
        },
        startTimer() {
            // Start the countdown timer
            this.timerInterval = setInterval(() => {
                if (this.timer > 0) {
                    this.timer--;
                } else {
                    // Timer expired, submit the quiz
                    clearInterval(this.timerInterval);
                    this.sendanswers();
                }
            }, 1000); // Decrement every second
        }
    },
    mounted() {
        this.fetchQuestions();
        this.startTimer(); // Start the timer when the component is mounted
    },
    beforeUnmount() {
        // Clear the timer interval when the component is destroyed
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
        }
    }
};
</script>

<style>
#quiz_container {
    margin-top: 5rem;
}

#question_box {
    border-radius: 2rem;
    border-color: black;
    border-style: solid;
    width: 100%;
}

#timer {
    font-size: 1.5rem;
    color: #ff0000; /* Red color for the timer */
}
</style>