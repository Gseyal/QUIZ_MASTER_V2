<!-- filepath: c:\Users\seyal\OneDrive\Desktop\QUIZ_MASTER_V2\app_frontend\src\views\stat.vue -->
<template>
    <div id="report_box">
        <div>
            <h1>Marksheet Report</h1>
            <div v-if="report">
                <div class="info">
                    <p><strong>Name:</strong> {{ report.name }}</p>
                    <p><strong>User ID:</strong> {{ report.user_id }}</p>
                    <p><strong>Date:</strong> {{ report.current_date }}</p>
                </div>
                <table class="table">
                    <thead>
                        <tr>
                            <th>Subject</th>
                            <th>Total Chapters</th>
                            <th>Attempted Chapters</th>
                            <th>Score</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="subject in report.subjects" :key="subject.name">
                            <td>{{ subject.name }}</td>
                            <td>{{ subject.total_chapters }}</td>
                            <td>{{ subject.attempted_chapters }}</td>
                            <td>{{ subject.score }}/{{ subject.outof }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div v-else>
                <p>Loading...</p>
            </div>
        </div>
    </div>

</template>

<script>
import { mapGetters } from 'vuex';

export default {
    data() {
        return {
            report: null,
        };
    },
    computed: {
        ...mapGetters(['id'])
    },
    created() {
        this.fetchReport();
    },
    methods: {
        async fetchReport() {
            try {
                const response = await fetch('http://localhost:5000/stat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ id: this.id })
                });
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                this.report = await response.json();
            } catch (error) {
                console.error('Error fetching report:', error);
            }
        },
    },
};
</script>

<style>
#report_box{
    margin-top: 5rem;
}
.info {
    margin-bottom: 20px;
}

.table {
    width: 100%;
    border-collapse: collapse;
}

.table th,
.table td {
    border: 1px solid #ccc;
    padding: 10px;
    text-align: left;
}

.table th {
    background-color: #f9f9f9;
}
</style>