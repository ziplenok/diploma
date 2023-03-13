<template>
  <div class="calculator-container">
    <form action="" class="form">
      <div class="field mrg-b">
        <h1 class="has-text-centered is-size-1 is-size-3-mobile has-text-white">
          Узнать шанс
        </h1>
      </div>

      <div class="field mrg-b">
        <label class="label is-size-4 is-size-6-mobile"
          >Выбирите 2 профильных предмета</label
        >
        <button
          class="button is-medium is-fullwidth btn-shadow is-size-6-mobile"
          type="button"
          @click="openSubjectModal"
        >
          Выбрать
        </button>
      </div>

      <Teleport to="body">
        <div class="modal" :class="{ 'is-active': isActiveSelectSubject }">
          <div class="modal-background"></div>
          <div class="modal-card">
            <header class="modal-card-head">
              <input
                class="input is-medium is-fullwidth"
                type="text"
                placeholder="Ввидите название предметов..."
                v-model="searchText"
              />
              <button
                class="delete"
                type="button"
                aria-label="close"
                @click="closeSubjectModal"
              ></button>
            </header>
            <section class="modal-card-body">
              <div class="list has-hoverable-list-items">
                <div
                  v-for="subject in subjectList"
                  :key="subjects.subjectCombinations.id"
                >
                  <div
                    class="list-item"
                    @click="
                      selectSubjectCombination(subject.first, subject.second)
                    "
                  >
                    <div class="list-item-title">
                      {{ subject.first }} + {{ subject.second }}
                    </div>
                  </div>
                </div>
              </div>
            </section>
            <footer class="modal-card-foot">
              <!-- <button class="button is-success">Save changes</button>
            <button class="button">Cancel</button> -->
            </footer>
          </div>
        </div>
      </Teleport>
      <!-- <div id="input" class="margin-bottom">
        <input
          class="input is-medium is-fullwidth"
          type="text"
          placeholder="Ввидите название предметов..."
          @focus="isVisibleSubjectOptions = true"
          v-model="searchText"
        />

        <div
          class="list has-hoverable-list-items"
          v-if="isVisibleSubjectOptions"
        >
          <div
            v-for="subject in subjects.subjectCombinations"
            :key="subjects.subjectCombinations.id"
          >
            <div
              class="list-item"
              @click="selectSubjectCombination(subject.first, subject.second)"
            >
              <div class="list-item-title">
                {{ subject.first }} + {{ subject.second }}
              </div>
            </div>
          </div>
        </div>
      </div> -->

      <div class="flex">
        <div class="inline-flex margin-bottom" v-if="isSelectedSubject">
          <span class="seleted-option">
            {{ firstSelected }} и {{ secondSelected }}
          </span>
          <font-awesome-icon
            icon="fa-solid fa-xmark"
            class="icon delete-selected-subject"
            @click="clearSelectedSubject"
          />
        </div>
      </div>

      <div class="field mrg-b">
        <label class="label is-size-4 is-size-6-mobile"
          >Укажите свою специальность</label
        >
        <button
          class="button is-medium is-fullwidth btn-shadow is-size-6-mobile"
          type="button"
          @click="openSpecialityModal"
        >
          Выбрать
        </button>
      </div>

      <Teleport to="body">
        <div class="modal" :class="{ 'is-active': isActiveSelectSpeciality }">
          <div class="modal-background"></div>
          <div class="modal-card">
            <header class="modal-card-head">
              <input
                class="input is-medium is-fullwidth"
                type="text"
                placeholder="Ввидите название специальности..."
                v-model="searchText"
              />
              <button
                class="delete"
                type="button"
                aria-label="close"
                @click="closeSpecialityModal"
              ></button>
            </header>
            <section class="modal-card-body">
              <div class="list has-hoverable-list-items">
                <div
                  v-for="subject in subjectList"
                  :key="subjects.subjectCombinations.id"
                >
                  <div
                    class="list-item"
                    @click="
                      selectSubjectCombination(subject.first, subject.second)
                    "
                  >
                    <div class="list-item-title">
                      {{ subject.first }} + {{ subject.second }}
                    </div>
                  </div>
                </div>
              </div>
            </section>
            <footer class="modal-card-foot">
              <!-- <button class="button is-success">Save changes</button>
            <button class="button">Cancel</button> -->
            </footer>
          </div>
        </div>
      </Teleport>

      <div class="flex mrg-b">
        <div class="inline-flex margin-bottom" v-if="isSelectedSpeciality">
          <span class="seleted-option">
            {{ firstSelected }} и {{ secondSelected }}
          </span>
          <font-awesome-icon
            icon="fa-solid fa-xmark"
            class="icon delete-selected-subject"
            @click="clearSelectedSubject"
          />
        </div>
      </div>

      <div class="field choose-radio has-text-centered mrg-b mrg-t">
        <div class="columns">
          <div class="column">
            <p class="is-size-5 has-text-white is-size-5 is-size-6-mobile">
              Выберите квоту
            </p>

            <div class="is-flex is-justify-content-space-evenly">
              <input
                class="is-checkradio is-rtl"
                id="radioBtn-1"
                type="radio"
                checked="checked"
              />
              <label
                for="qouta-1 has-text-white"
                class="has-text-white is-size-7-mobile"
                >общая</label
              >

              <input
                class="is-checkradio is-rtl"
                id="radioBtn-2"
                type="radio"
              />
              <label
                for="qouta-2 has-text-white"
                class="has-text-white is-size-7-mobile"
                >сельская</label
              >
            </div>
          </div>

          <div class="column">
            <p class="is-size-5 has-text-white is-size-5 is-size-6-mobile">
              Преимущественные права
            </p>

            <div class="is-flex is-justify-content-space-evenly">
              <input
                class="is-checkradio is-rtl"
                id="radioBtn-3"
                type="radio"
                checked="checked"
              />
              <label
                for="prem-prava-1 has-text-white"
                class="has-text-white is-size-7-mobile"
                >нет</label
              >
              <input
                class="is-checkradio is-rtl"
                id="radioBtn-4"
                type="radio"
              />
              <label for="prem-prava-2" class="has-text-white is-size-7-mobile"
                >ЭНПС</label
              >
            </div>
          </div>
        </div>
      </div>

      <!-- <div class="columns choose">
        <div class="column">
          <div class="control">
            <p class="choose-heading is-size-5">Выберите квоту</p>
            <div class="columns">
              <label class="radio column">
                <input
                  class="is-checkradio is-medium is-white"
                  id="exampleRadioMedium"
                  type="radio"
                  checked="checked"
                />
                <label class="text">общая</label>
              </label>
              <label class="radio column">
                <input
                  class="is-checkradio is-medium is-white"
                  id="exampleRadioMedium"
                  type="radio"
                />
                <label class="text">сельская</label>
              </label>
            </div>
          </div>
        </div>

        <div class="is-divider-vertical"></div>

        <div class="filed"></div>
        <div class="column">
          <div class="control">
            <p class="choose-heading">Преимущественные права</p>
            <div class="columns">
              <label class="radio column">
                <input
                  class="is-checkradio is-medium is-white"
                  id="exampleRadioMedium"
                  type="radio"
                  checked="checked"
                />
                <label class="text">нет</label>
              </label>
              <label class="radio column">
                <input
                  class="is-checkradio is-medium is-white"
                  id="exampleRadioMedium"
                  type="radio"
                />
                <label class="text">ЭНПС</label>
              </label>
            </div>
          </div>
        </div>
      </div> -->

      <div class="field px-3">
        <p class="has-text-centered has-text-white is-size-4 is-size-6-mobile">
          Укажите балл ЕНТ
        </p>

        <div class="level has-text-centered">
          <span class="level-left is-paddingless mr-3 has-text-white">0</span>
          <div class="level-item is-inline">
            <input
              id="sliderWithValue"
              class="slider has-output is-circle is-white is-fullwidth"
              min="0"
              max="100"
              v-model="value"
              step="1"
              type="range"
            />
            <output for="sliderWithValue" class="level-right bubble">50</output>
          </div>

          <span class="ml-3 has-text-white">140</span>
        </div>
      </div>

      <p
        class="has-text-centered has-text-white mb-6 is-size-4 is-size-6-mobile"
      >
        Выбирите баллы по профильным предметам
      </p>

      <!-- <div class="columns is-centered"> -->

      <div
        class="is-flex is-justify-content-space-between is-align-items-center mrg-b prof-wrapper"
      >
        <input class="input prof-input" type="text" v-model="inputOne" />
        <font-awesome-icon icon="fa-solid fa-plus" class="fa-icon mx-3" />
        <input class="input prof-input" type="text" v-model="inputTwo" />
        <font-awesome-icon icon="fa-solid fa-equals" class="fa-icon mx-3" />
        <div class="is-size-1 has-text-white">{{ result }}</div>
      </div>

      <!-- </div> -->

      <div class="is-flex is-justify-content-center my-5">
        <button class="result button is-medium btn-shadow">
          Показать результат
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
/*
  imports
*/

import { ref, computed, watch, onMounted } from "vue";
import { useSubjectsStore } from "@/stores/subjects.js";

/*
  subjects
*/

const isActiveSelectSubject = ref(false),
  isSelectedSubject = ref(false),
  searchText = ref(""),
  firstSelected = ref(""),
  secondSelected = ref("");

const subjects = useSubjectsStore();

const selectSubjectCombination = (first, second) => {
  firstSelected.value = first;
  secondSelected.value = second;
  isActiveSelectSubject.value = false;
  isSelectedSubject.value = true;
  closeSubjectModal();
};

const openSubjectModal = () => {
  isActiveSelectSubject.value = true;
};

const closeSubjectModal = () => {
  isActiveSelectSubject.value = false;
  searchText.value = "";
};

const subjectList = computed(() => {
  if (searchText.value.trim().length > 0) {
    return subjects.subjectCombinations.filter((subject) =>
      subject.first
        .toLowerCase()
        .includes(searchText.value.trim().toLowerCase())
    );
  }
  return subjects.subjectCombinations;
});

const clearSelectedSubject = () => {
  firstSelected.value = "";
  secondSelected.value = "";
  isSelectedSubject.value = false;
};

/*
  specialities
*/

const isActiveSelectSpeciality = ref(false),
  isSelectedSpeciality = ref(false);

const openSpecialityModal = () => {
  isActiveSelectSpeciality.value = true;
};

const closeSpecialityModal = () => {
  isActiveSelectSpeciality.value = false;
};

/*
  slider
*/

/*
  UNT profile subject input
*/

const inputOne = ref(""),
  inputTwo = ref(""),
  result = ref(0);

watch([inputOne, inputTwo], () => summInputs(inputOne, inputTwo));

let summInputs = (inputOne, inputTwo) => {
  let input1, input2;

  if (inputOne.value === "") input1 = 0;
  if (inputTwo.value === "") input2 = 0;

  input1 = parseInt(inputOne.value);
  input2 = parseInt(inputTwo.value);

  if (input1 >= 0 && input2 >= 0) {
    result.value = input1 + input2;
  }

  // if (
  //   Number.isInteger(inputOne) &&
  //   Number.isInteger(inputTwo) &&
  //   inputOne > 0 &&
  //   inputTwo > 0
  // ) {

  // }
};
</script>

<style scope lang="scss">
$has-text-white: #ffffff;
$mrg-large: 40px;
$mrg-small: 40px;

@import "@/assets/main.scss";

.mrg-b {
  @include mobile {
    margin-bottom: $mrg-small !important;
  }
  @include tablet {
    margin-bottom: $mrg-small !important;
  }

  @include desktop {
    margin-bottom: $mrg-large !important;
  }
}

.btn-shadow {
  filter: drop-shadow(0px 8px 7px rgba(0, 0, 0, 0.25));
}

// .mrg-t {
//   @include desktop {
//     margin-top: 80px;
//   }
// }
.calculator-container {
  background: linear-gradient(
    231.45deg,
    rgba(51, 0, 159, 0.85) 5.16%,
    rgba(54, 35, 202, 0.932297) 29.15%,
    rgba(48, 51, 188, 0.946543) 34.9%,
    #196d88 56.51%,
    #029482 93.02%
  );
  @include mobile {
    padding: 8px 12px;
  }
  @include tablet-only {
    padding: 67px 180px;
  }
  @include desktop {
    padding: 64px 0;
  }
}

.form {
  // padding: 50px 120px 72px 120px;
  margin: 0 auto;
  background: linear-gradient(
    180deg,
    rgba(0, 181, 221, 0.34) 0%,
    rgba(207, 207, 207, 0.15) 100%
  );

  box-shadow: rgba(0, 0, 0, 0.19) 0px 10px 20px, rgba(0, 0, 0, 0.23) 0px 6px 6px;
  border-radius: 0.813rem;

  @include touch {
    padding: 48px 16px;
  }

  @include desktop {
    max-width: 1010px;
    padding: 50px 120px 72px 120px;
  }
}

// .flex {
//   display: flex;
//   justify-content: center;
// }

// #input {
//   position: relative;
//   display: inline-block;
//   width: 100%;
// }

/* .list {
  max-height: 250px;
  position: absolute;
  left: 0;
  width: 100%;
  font-size: 18px;
  background: #ffffff;
  border-radius: 3px;
  z-index: 999;
  box-shadow: rgba(255, 255, 255, 0.1) 0px 1px 1px 0px inset,
    rgba(50, 50, 93, 0.25) 0px 50px 100px -20px,
    rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
  overflow: auto;
} */

.list-item {
  cursor: pointer;
}

.list::-webkit-scrollbar {
  width: 16px;
}

.list::-webkit-scrollbar-track {
  background-color: #e4e4e4;
  border-radius: 3px;
}

.list::-webkit-scrollbar-thumb {
  background-image: linear-gradient(180deg, #d0368a 0%, #708ad4 99%);
  border-radius: 3px;
}

.inline-flex {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  background: #ffffff;
  box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 6px, rgba(0, 0, 0, 0.23) 0px 3px 6px;
  border-radius: 100px;
  padding: 3px 0 3px 15px;
}

.seleted-option {
  display: inline-block;
  margin-right: 9px;
}

.delete-selected-subject {
  display: inline-block;
  padding-right: 15px;
  cursor: pointer;
}

.choose-radio {
  background: rgba(0, 6, 9, 0.26);
  border-radius: 8px;
}
.range-wrap {
  display: inline-block;
  position: relative;
}

.fa-icon {
  width: 34px;
  height: 34px;
  color: #ffffff;
}

.prof-wrapper {
  @include tablet {
    padding: 0 100px;
  }
}

.prof-input {
  max-width: 185px;
}

.bubble {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}

.result {
  background: linear-gradient(
    90deg,
    #d00000 0%,
    #d3004c 34.94%,
    rgba(255, 0, 77, 0.8) 65.8%,
    #ff8310 100%
  );
  box-shadow: 0px 8px 7px rgba(0, 0, 0, 0.3);
  border-radius: 8px;
  border: none;
}
</style>
