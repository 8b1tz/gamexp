<template>
  <v-card class="pa-6">
    <v-row v-if="Object.keys(data).length === 0"> ... </v-row>
    <v-row>
      <v-col cols="4" lg="4" md="4" sm="12" xs="12">
        <v-img :width="450" :src="data.thumbnail" class="mb-4"></v-img>

        <div v-for="(item, index) in data" :key="index" class="mb-2">
          <div v-if="!doNotShow.includes(index)">
            <span class="key_info pa-2"> {{ index }}: </span>
            <span class="value_info ml-3">
              {{ item }}
            </span>
          </div>
        </div>

        <span class="pa-2 mt-1">Status: </span>
        <span>
          <v-icon :color="data.status == 'Live' ? 'green' : 'red'" small>
            mdi-circle
          </v-icon>
        </span>
      </v-col>

      <v-col cols="8" lg="8" md="8" sm="12" xs="12">
        <div>
          <div>{{ data.description }}</div>
        </div>

        <div v-if="data.minimum_system_requirements" class="my-10">
          <div class="mb-4">Minimum requirements</div>
          <v-simple-table dense>
            <template v-slot:default>
              <tbody>
                <tr
                  v-for="(item, index) in data.minimum_system_requirements"
                  :key="index"
                >
                  <td class="key_info">{{ index }}</td>
                  <td>{{ item }}</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </div>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "DetailsId",

  data() {
    return {
      data: {},

      rating: 0,

      doNotShow: [
        "id",
        "thumbnail",
        "short_description",
        "description",
        "game_url",
        "freetogame_profile_url",
        "minimum_system_requirements",
        "screenshots",
        "status",
      ],
    };
  },

  methods: {
    ...mapActions("game", ["getGameById"]),

    goToSite(path) {
      window.open(path, "_blank");
    },
  },

  created() {
    this.getGameById(this.$route.params.id).then((resp) => {
      this.data = { ...resp };
    });
  },
};
</script>

<style>
.key_info {
  text-transform: capitalize;
}

.value_info {
  text-align: justify;
}
</style>
