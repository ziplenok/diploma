<script setup>
import { RouterLink, RouterView } from "vue-router";
import NavBar from "@/components/Layout/NavBar.vue";
</script>

<template>
  <NavBar />
  <RouterView />
</template>

<style lang="scss">
// @import "bulma/css/bulma.min.css";

// @import "bulma-divider";

// @import "bulma-slider";

// @import "bulma-checkradio/dist/css/bulma-checkradio.min.css";

// @import "bulma-tooltip/dist/css/bulma-tooltip.min.css";

// @import "bulma-list/css/bulma-list.css";

// @import url("https://fonts.googleapis.com/css2?family=Didact+Gothic&display=swap");

@import "node_modules/bulma/bulma.sass";
@import url("https://fonts.googleapis.com/css2?family=Didact+Gothic&display=swap");
@import "node_modules/bulma-checkradio/src/sass/index.sass";
@import "node_modules/bulma-slider/src/sass/index.sass";
@import "node_modules/bulma-list/sass/bulma-list.sass";
html {
  height: 100%;
}
body {
  min-height: 100%;
}
</style>
