<template>
    <div id="main">
        <div id="acont" class="container">
            <p style="font-weight: bold; font-size: large; text-decoration: underline;">Subject: {{ subject.title }}</p>
            <P>{{ subject.description }}</P>
        </div>
        <div id='bcont' class="container text-center">
            <div v-for="(chapter, chid) in subject.chapters" :key="chid" class="row">
                <div class="col order-first">
                    {{ chapter.chapter }}
                </div>
                <div class="col order-last">
                    <a v-if="client === 'admin'" @click.prevent="del_chapter(chapter.id)">Delete /</a>
                    <router-link :to="{ path: '/quiz', query: { subject: subject.title, chapter: chapter.id } }">Start -></router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    data() {
        return {
            title: this.$route.query.title || 'No Title',
            id: this.$route.query.id || 'NO id'
        };
    },
    watch: {
        '$route.query.title'(title) {
            this.title = title;
        },
        '$route.query.id'(id) {
            this.id = id;
        }
    },
    computed: {
        ...mapGetters(['sub_data', 'client']),
        subject() {
            if (Array.isArray(this.sub_data)) {
                return this.sub_data.find(subject => subject.title === this.title) || { description: '', chapters: [] };
            }
            return { description: '', chapters: [] };
        }
    },
    methods: {
        ...mapActions(['fetchlist', 'delete']),
        async del_chapter(chid) {
            const payload = {
                type: 'Chapter',
                id: chid // Use the passed chapter ID
            };
            console.log(payload)
            await this.delete(payload);
            this.fetchlist(); // Refresh the list after deletion
        }
    },
    mounted() {
        this.fetchlist();
    }
};
</script>

<style scoped>
#main {
    padding-top: 5rem;
}

.col {
    border-bottom: 2px;
    margin: 10px;
    border-color: black;
    border-style: solid;
}

.container {
    margin-bottom: 10px;
    border-color: black;
    border-style: solid;
}

#acont {
    width: 100%;
    height: 10rem;
}
</style>