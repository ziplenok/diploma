import { createRouter, createWebHistory } from "vue-router";
import ViewCalculator from "@/views/ViewCalculator.vue";
import ViewSpecialities from "@/views/ViewSpecialities.vue";
import ViewUniversities from "@/views/ViewUniversities.vue";
import UniversityPage from "@/views/UniversityPage.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: ViewCalculator,
    },
    {
      path: "/specialities",
      name: "specialities",
      component: ViewSpecialities,
    },
    {
      path: "/universities",
      name: "universities",
      component: ViewUniversities,
    },
    {
      path: "/univerities/test",
      name: "test",
      component: UniversityPage,
    },
  ],
});

export default router;
