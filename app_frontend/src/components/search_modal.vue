<template>
    <div class="modal fade" id="example2Modal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <div class="input-group input-group-lg">
                        <span class="input-group-text" id="inputGroup-sizing-lg">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                                <path
                                    d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0" />
                            </svg>
                        </span>
                        <input v-model="quest" @input="search" type="text" class="form-control" aria-label="Sizing example input"
                            aria-describedby="inputGroup-sizing-lg">
                    </div>
                </div>
                <div class="modal-body">
                    <div v-for="result in searchResults" :key="result.id" class="mb-2">
                        <router-link :to="result.link" class="btn btn-primary">{{ result.label }}</router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
    data() {
        return {
            quest: null, // User's search query
            searchResults: [] // Array to store search results
        };
    },
    computed: {
        ...mapGetters(['sub_data']) // Get 'sub_data' from Vuex store
    },
    methods: {
        search() {
            this.searchResults = []; // Use 'this' to refer to the data property
            if (this.quest.trim() === '') {
                return;
            }

            const query = this.quest.toLowerCase();

            this.sub_data.forEach(subject => {
                if (subject.title.toLowerCase().includes(query)) {
                    this.searchResults.push({
                        id: subject.id,
                        label: `Subject: ${subject.title}`,
                        link: { path: '/chapter', query: { title: subject.title, id: subject.id } }
                    });
                }

                subject.chapters.forEach(chapter => {
                    if (chapter.chapter.toLowerCase().includes(query)) {
                        this.searchResults.push({
                            id: chapter.id,
                            label: `Chapter: ${chapter.chapter}`,
                            link: { path: '/quiz', query: { subject: subject.title, chapter: chapter.id } }
                        });
                    }
                });
            });
        }
    }
};
</script>