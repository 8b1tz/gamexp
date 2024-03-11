<template>
  <v-app-bar absolute color="dray darken-4" dark elevation="0">
    <v-btn elevation="0" height="100%" @click="goTo(enumRoutes.HOME)">
      Home
    </v-btn>
    <v-spacer></v-spacer>
    <v-btn elevation="0" height="100%" @click="goTo(enumRoutes.GAMES)">
      Games
    </v-btn>
    <v-btn elevation="0" height="100%" @click="goTo(enumRoutes.STATISTICS)">
      Dashboard
    </v-btn>
  </v-app-bar>
</template>

<script>
export default {
  data: () => ({
    enumRoutes: {
      HOME: "/home",
      GAMES: "/",
      STATISTICS: "/dashboard",
      FAVORITE: "/favorite",
    },
  }),

  methods: {
    goTo(path) {
      this.$router.push({ path });
    },
  },
};
</script>

<style></style>
