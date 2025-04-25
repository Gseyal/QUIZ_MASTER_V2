<template>
  <div>
    <button type="button" class="circle_button" data-bs-toggle="modal" data-bs-target="#exampleModal">
      +
    </button>

    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">

            <nav>
              <div class="nav nav-tabs" id="main-tab" role="tablist">
                <button class="nav-link active" id="nav-new-tab" data-bs-toggle="tab" data-bs-target="#nav-new"
                  type="button" role="tab" aria-controls="nav-new" aria-selected="true">NEW RECORD</button>
                <button class="nav-link" id="nav-update-tab" data-bs-toggle="tab" data-bs-target="#nav-update"
                  type="button" role="tab" aria-controls="nav-update" aria-selected="false">UPDATE RECORD</button>
              </div>
            </nav>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>

          <div class="modal-body">
            <div class="tab-content" id="main-tabContent">

              <div class="tab-pane fade show active" id="nav-new" role="tabpanel" aria-labelledby="nav-new-tab">
                <nav>
                  <div class="nav nav-tabs" id="new-tab" role="tablist">
                    <button class="nav-link active" id="nav-new-subject" data-bs-toggle="tab"
                      data-bs-target="#new-subject" type="button" role="tab" aria-controls="new-subject"
                      aria-selected="true">Subject</button>
                    <button class="nav-link" id="nav-new-chapter" data-bs-toggle="tab" data-bs-target="#new-chapter"
                      type="button" role="tab" aria-controls="new-chapter" aria-selected="false">Chapter</button>
                    <button class="nav-link" id="nav-new-question" data-bs-toggle="tab" data-bs-target="#new-question"
                      type="button" role="tab" aria-controls="new-question" aria-selected="false">Question</button>
                  </div>
                </nav>
                <div class="tab-content" id="new-tabContent">
                  <div class="tab-pane fade show active" id="new-subject" role="tabpanel"
                    aria-labelledby="nav-new-subject">
                    <subject_add mode="add" @refresh="$emit('refresh')"></subject_add>
                  </div>
                  <div class="tab-pane fade" id="new-chapter" role="tabpanel" aria-labelledby="nav-new-chapter">
                    <chapter_add mode="add" @refresh="$emit('refresh')"></chapter_add>
                  </div>
                  <div class="tab-pane fade" id="new-question" role="tabpanel" aria-labelledby="nav-new-question">
                    <question_add mode="add" @refresh="$emit('refresh')"></question_add>
                  </div>
                </div>
              </div>

              <div class="tab-pane fade" id="nav-update" role="tabpanel" aria-labelledby="nav-update-tab">
                <nav>
                  <div class="nav nav-tabs" id="update-tab" role="tablist">
                    <button class="nav-link active" id="nav-update-subject" data-bs-toggle="tab"
                      data-bs-target="#update-subject" type="button" role="tab" aria-controls="update-subject"
                      aria-selected="true">U-Subject</button>
                    <button class="nav-link" id="nav-update-chapter" data-bs-toggle="tab"
                      data-bs-target="#update-chapter" type="button" role="tab" aria-controls="update-chapter"
                      aria-selected="false">U-Chapter</button>
                    <button class="nav-link" id="nav-update-question" data-bs-toggle="tab"
                      data-bs-target="#update-question" type="button" role="tab" aria-controls="update-question"
                      aria-selected="false">U-Question</button>
                  </div>
                </nav>
                <div class="tab-content" id="update-tabContent">
                  <div class="tab-pane fade show active" id="update-subject" role="tabpanel"
                    aria-labelledby="nav-update-subject">
                    <subject_update mode="update" @refresh="$emit('refresh')"></subject_update>
                  </div>
                  <div class="tab-pane fade" id="update-chapter" role="tabpanel" aria-labelledby="nav-update-chapter">
                    <chapter_update mode="update" @refresh="$emit('refresh')"></chapter_update>
                  </div>
                  <div class="tab-pane fade" id="update-question" role="tabpanel" aria-labelledby="nav-update-question">
                    <question_update mode="update" @refresh="$emit('refresh')"></question_update>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapGetters } from 'vuex';
import subject_add from './subject_add.vue';
import chapter_add from './chapter_add.vue'
import question_add from './question_add.vue'
import subject_update from '../components/subject_update.vue'
import chapter_update from '../components/chapter_update.vue'
import question_update from '../components/question_update.vue'
export default {
  components: {
    subject_update_id:null,
    subject_add,
    chapter_add,
    question_add,
    subject_update,
    chapter_update,
    question_update
  },
  computed: {
    ...mapGetters(['sub_data'])
  }
}
</script>
<style>
.circle_button {
  padding: 1rem;
  border-radius: 50%;
  position: fixed;
  bottom: 20px;
  right: 46%;
  z-index: 1001;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}
</style>