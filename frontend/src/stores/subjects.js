import { ref, computed, reactive } from "vue";
import { defineStore } from "pinia";

export const useSubjectsStore = defineStore("subjects", () => {
  // state: () => {
  //   return {
  //     subjectCombinations: [
  //       {
  //         id: 0,
  //         first: "математика",
  //         second: "физика",
  //       },
  //       {
  //         id: 1,
  //         first: "математика",
  //         second: "география",
  //       },
  //       {
  //         id: 2,
  //         first: "математика",
  //         second: "информатика",
  //       },
  //       {
  //         id: 3,
  //         first: "история",
  //         second: "география",
  //       },
  //       {
  //         id: 4,
  //         first: "биолгия",
  //         second: "химия",
  //       },
  //       {
  //         id: 5,
  //         first: "биолгия",
  //         second: "география",
  //       },
  //       {
  //         id: 6,
  //         first: "история",
  //         second: "иностранный язык",
  //       },
  //       {
  //         id: 7,
  //         first: "язык обучние и летаратура",
  //         second: "история",
  //       },
  //       {
  //         id: 8,
  //         first: "георграфия",
  //         second: "иностранный язык",
  //       },
  //       {
  //         id: 9,
  //         first: "химия",
  //         second: "физика",
  //       },
  //       {
  //         id: 10,
  //         first: "творческий",
  //         second: "творческий",
  //       },
  //     ],
  //   };
  // };
  const subjectCombinations = reactive([
    {
      id: 0,
      first: "математика",
      second: "физика",
    },
    {
      id: 1,
      first: "математика",
      second: "география",
    },
    {
      id: 2,
      first: "математика",
      second: "информатика",
    },
    {
      id: 3,
      first: "история",
      second: "география",
    },
    {
      id: 4,
      first: "биолгия",
      second: "химия",
    },
    {
      id: 5,
      first: "биолгия",
      second: "география",
    },
    {
      id: 6,
      first: "история",
      second: "иностранный язык",
    },
    {
      id: 7,
      first: "язык обучние и летаратура",
      second: "история",
    },
    {
      id: 8,
      first: "георграфия",
      second: "иностранный язык",
    },
    {
      id: 9,
      first: "химия",
      second: "физика",
    },
    {
      id: 10,
      first: "творческий",
      second: "творческий",
    },
  ]);

  return { subjectCombinations };
});
