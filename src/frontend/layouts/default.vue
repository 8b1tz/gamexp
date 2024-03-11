<template>
  <v-app dark class="app">
    <Menu />
    <v-main>
      <v-container>
        <Nuxt class="mt-14" />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Menu from "@/components/Common/Menu.vue";

export default {
  name: "DefaultLayout",

  components: { Menu },

  data() {
    return {};
  },
};
</script>

<style>
.app {
  font-family: "Pixelify Sans", sans-serif !important;
  font-optical-sizing: auto;
}
</style>
