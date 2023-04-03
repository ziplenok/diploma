import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

/* import the fontawesome core */
import { library } from "@fortawesome/fontawesome-svg-core";

/* import font awesome icon component */
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

/* import specific icons */
import {
  faPlus,
  faEquals,
  faXmark,
  faCity,
  faAngleDown,
  faMagnifyingGlass,
} from "@fortawesome/free-solid-svg-icons";

library.add(faPlus);
library.add(faEquals);
library.add(faXmark);
library.add(faCity);
library.add(faAngleDown);
library.add(faMagnifyingGlass);

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

const vuetify = createVuetify({
  components,
  directives,
});

const app = createApp(App);

app.component("font-awesome-icon", FontAwesomeIcon);
app.use(vuetify);
app.use(createPinia());
app.use(router);

app.mount("#app");
