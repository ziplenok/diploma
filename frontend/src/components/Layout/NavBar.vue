<template>
  <nav class="navbar" aria-label="main navigation" role="navigation">
    <div class="navbar-brand">
      <div class="navbar-item is-size-4">Streamlet</div>

      <a
        @click.prevent="showMobileNav = !showMobileNav"
        class="navbar-burger"
        :class="{ 'is-active': showMobileNav }"
        aria-expanded="false"
        aria-label="menu"
        data-target="navbarBasicExample"
        role="button"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div
      id="navbarBasicExample"
      class="navbar-menu"
      :class="{ 'is-active': showMobileNav }"
    >
      <div class="navbar-start">
        <RouterLink to="/" class="navbar-item" active-class="is-active">
          шансы
        </RouterLink>
        <RouterLink
          to="/specialities"
          class="navbar-item"
          active-class="is-active"
        >
          специальности
        </RouterLink>
        <RouterLink
          to="/universities"
          class="navbar-item"
          active-class="is-active"
        >
          список ВУЗов
        </RouterLink>
      </div>
    </div>
  </nav>
</template>

<script setup>
/*
  imports
*/
import { ref } from "vue";
/*
  mobile nav
*/
const showMobileNav = ref(false);
</script>

<style scoped lang="scss">
@import "@/assets/main.scss";
// .navbar-menu
// {
// 	background-color: #060D01;
// 	color: #FFFFFF;
// }

@media (max-width: 1023px) {
  .navbar-menu {
    position: absolute;
    left: 0;
    width: 100%;
  }
}
</style>
