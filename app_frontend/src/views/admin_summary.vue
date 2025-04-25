<template>
    <div class="admin-summary">
        <!-- Display Total Users -->
        <div class="summary-box">
            <h2>No. of Users</h2>
            <p>{{ userCount }}</p>
        </div>

        <!-- Display Subjects and Total Chapters -->
        <div class="summary-box">
            <h2>Subjects and Total Chapters</h2>
            <ul>
                <li v-for="subject in subjects" :key="subject.name">
                    {{ subject.name }}: {{ subject.chapter_count }}
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            userCount: 0, // Total number of users
            subjects: []  // List of subjects with chapter counts
        };
    },
    methods: {
        async fetchSummaryData() {
            try {
                const response = await fetch('http://127.0.0.1:5000/admin_summary'); // Replace with your API endpoint
                const data = await response.json();
                this.userCount = data.user_count;
                this.subjects = data.subjects;
            } catch (error) {
                console.error('Error fetching summary data:', error);
            }
        }
    },
    mounted() {
        this.fetchSummaryData(); // Fetch data when the component is mounted
    }
};
</script>

<style>
.admin-summary {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
}

.summary-box {
    background-color: #f8f9fa;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    text-align: center;
    margin-bottom: 20px;
    width: 300px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.summary-box h2 {
    font-size: 24px;
    margin-bottom: 10px;
    color: #333;
}

.summary-box p {
    font-size: 32px;
    margin: 0;
    color: #007bff;
}

.summary-box ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.summary-box li {
    font-size: 18px;
    color: #555;
    margin: 5px 0;
}
</style>