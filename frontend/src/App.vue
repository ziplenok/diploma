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

@import "bulma-divider";

@import "bulma-slider";

@import "bulma-checkradio/dist/css/bulma-checkradio.min.css";

@import "bulma-tooltip/dist/css/bulma-tooltip.min.css";

@import "bulma-list/css/bulma-list.css";

@import url("https://fonts.googleapis.com/css2?family=Didact+Gothic&display=swap");

body {
  font-family: "Didact Gothic", sans-serif;
}
</style>
