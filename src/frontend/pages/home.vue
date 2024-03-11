<template>
  <div>
    <v-card
      :img="require(`~/static/home_image.png`)"
      color="transparent"
      elevation="0"
      class="cardHome d-flex flex-wrap mx-auto h-100"
    >
      <v-col>
        <v-card class="cardTitle">
          <div class="title_game py-10">GAME XP APP</div>
        </v-card>
      </v-col>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "Home",
};
</script>

<style scoped>
.title_game {
  margin-top: 30vh !important;
  text-align: center;
  font-size: 60px !important;
  opacity: 1 !important;
}

.cardHome {
  height: calc(100vh - 100px);
}


.h-100 {
  max-height: 100% !important;
}

</style>
