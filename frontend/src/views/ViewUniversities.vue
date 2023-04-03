<template>
  <div class="universities-container">
    <div class="columns">
      <TopSectionBottomRounded>
        <div class="column mt-6">
          <div class="is-flex is-align-content-center mb-4">
            <p class="is-size-6-mobile has-text-white mr-3">Укажите город</p>
            <div class="dropdown"></div>
            <div class="dropdown-trigger">
              <button
                class="button trigger is-small is-rounded"
                aria-haspopup="true"
                aria-controls="dropdown-menu"
              >
                <font-awesome-icon icon="fa-solid fa-city" />
                <span class="icon is-small">
                  <font-awesome-icon icon="fa-solid fa-angle-down" />
                </span>
              </button>
            </div>
          </div>
          <div class="field">
            <p class="control has-icons-left has-icons-right">
              <input
                class="input is-rounded has-text-white"
                type="text"
                placeholder="Поиск..."
              />

              <span class="icon is-small is-right">
                <font-awesome-icon :icon="['fas', 'magnifying-glass']" />
              </span>
            </p>
          </div>
        </div>
      </TopSectionBottomRounded>
      <MainSectionBase>
        <template #main-section>
          <div class="column">
            <div class="card mb-3">
              <header class="card-header">
                <p class="card-header-title">Алматы</p>
                <button class="card-header-icon" aria-label="more options">
                  <span class="icon">
                    <font-awesome-icon icon="fa-solid fa-angle-down" />
                  </span>
                </button>
              </header>
            </div>

            <div class="card mb-3">
              <header class="card-header">
                <p class="card-header-title">Астана</p>
                <button class="card-header-icon" aria-label="more options">
                  <span class="icon">
                    <font-awesome-icon icon="fa-solid fa-angle-down" />
                  </span>
                </button>
              </header>
            </div>

            <div class="card mb-3">
              <header class="card-header">
                <p class="card-header-title">Акмолинская область</p>
                <button class="card-header-icon" aria-label="more options">
                  <span class="icon">
                    <font-awesome-icon icon="fa-solid fa-angle-down" />
                  </span>
                </button>
              </header>
            </div>

            <div class="card mb-3">
              <header class="card-header">
                <p class="card-header-title">Актюбинская область</p>
                <button class="card-header-icon" aria-label="more options">
                  <span class="icon">
                    <font-awesome-icon icon="fa-solid fa-angle-down" />
                  </span>
                </button>
              </header>
            </div>

            <div class="card mb-3">
              <header class="card-header">
                <p class="card-header-title">Алматинская область</p>
                <button class="card-header-icon" aria-label="more options">
                  <span class="icon">
                    <font-awesome-icon icon="fa-solid fa-angle-down" />
                  </span>
                </button>
              </header>
            </div>

            <div class="card mb-3">
              <header class="card-header">
                <p class="card-header-title">Атырауская область</p>
                <button class="card-header-icon" aria-label="more options">
                  <span class="icon">
                    <font-awesome-icon icon="fa-solid fa-angle-down" />
                  </span>
                </button>
              </header>
            </div>

            <div class="card mb-3">
              <header class="card-header">
                <p class="card-header-title">Восточно-Казахстанская область</p>
                <button class="card-header-icon" aria-label="more options">
                  <span class="icon">
                    <font-awesome-icon icon="fa-solid fa-angle-down" />
                  </span>
                </button>
              </header>
            </div>

            <div class="card mb-3">
              <header class="card-header">
                <p class="card-header-title">Жамбылская область</p>
                <button class="card-header-icon" aria-label="more options">
                  <span class="icon">
                    <font-awesome-icon icon="fa-solid fa-angle-down" />
                  </span>
                </button>
              </header>
            </div>

            <div class="card mb-3">
              <header class="card-header" @click="toggleUniversityList()">
                <p class="card-header-title">Карагандинская область</p>
                <button class="card-header-icon" aria-label="more options">
                  <span class="icon">
                    <font-awesome-icon icon="fa-solid fa-angle-down" />
                  </span>
                </button>
              </header>
              <div v-if="isOpenedUniversityList">
                <div class="field has-addons">
                  <span class="control is-expanded">
                    <a class="button is-block is-selected-blue"> Караганда </a>
                  </span>
                  <span class="control is-expanded">
                    <a class="button is-block"> Темиртау </a>
                  </span>
                  <span class="control is-expanded">
                    <a class="button is-block"> Жезказган </a>
                  </span>
                </div>

                <div class="card-content">
                  <div class="content">
                    <div class="list">
                      <RouterLink
                        class="list-item"
                        to="/univerities/test"
                        active-class="is-active"
                      >
                        <div class="list-item-title mb-2">
                          Карагандинский государственный университет имени
                          академика Е.Букетова (КарГУ им. Букетова)
                        </div>
                        <div class="flex-description">
                          <span class="is-size-7-mobile has-text-black">
                            Колличество образовательныx программ: 10
                          </span>
                          <span class="is-size-7-mobile has-text-black"
                            >Проходной балл: 50</span
                          >
                        </div>
                      </RouterLink>
                      <div class="list-item">
                        <div class="list-item-title mb-2">
                          Карагандинский технический университет (Карагандинский
                          государственный технический университет)
                        </div>
                        <div class="flex-description">
                          <span class="is-size-7-mobile">
                            Колличество образовательныx программ: 10
                          </span>
                          <span class="is-size-7-mobile"
                            >Проходной балл: 50</span
                          >
                        </div>
                      </div>

                      <div class="list-item">
                        <div class="list-item-content">
                          <div class="list-item-title mb-2">
                            Карагандинский экономический университет
                            Казпотребсоюза (КЭУ Казпотребсоюза)
                          </div>
                          <div class="flex-description">
                            <span class="is-size-7-mobile">
                              Колличество образовательныx программ: 10
                            </span>
                            <span class="is-size-7-mobile"
                              >Проходной балл: 50</span
                            >
                          </div>
                        </div>
                      </div>
                      <div class="list-item">
                        <div class="list-item-content">
                          <div class="list-item-title mb-2">
                            Медицинский университет Караганды (КГМУ)
                          </div>
                          <div class="flex-description">
                            <span class="is-size-7-mobile">
                              Колличество образовательныx программ: 10
                            </span>
                            <span class="is-size-7-mobile"
                              >Проходной балл: 50</span
                            >
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
      </MainSectionBase>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from "vue";
import "@/components/Layout/TopSectionBottomRounded.vue";
import TopSectionBottomRounded from "../components/Layout/TopSectionBottomRounded.vue";
import MainSectionBase from "../components/Layout/MainSectionBase.vue";

/*
  card
*/

const isOpenedUniversityList = ref(false);

const toggleUniversityList = () => {
  isOpenedUniversityList.value = !isOpenedUniversityList.value;
};
</script>

<style scope lang="scss">
@import "@/assets/variables.scss";

.universities-container {
  // background: #5e1b51;
}

.trigger {
  background-color: transparent;
  color: white;
}

/*
list items
*/
.card {
  border-radius: 1rem;
}

.flex-description {
  display: flex;
  flex-direction: column;
}

.is-selected-blue {
  background-color: #ededed !important;
  color: #333 !important;
}
</style>
