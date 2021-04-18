<template>
  <v-carousel
    v-if="enabled"
    cycle
    height="200"
    hide-delimiter-background
    show-arrows-on-hover
  >
    <template v-if="photos">
      <v-carousel-item
        v-for="(photo, key) in photos"
        :key="key"
        :src="`${baseUrl}/${photo.url}`"
      />
    </template>
    <template v-else>
      <v-progress-circular :size="70" :width="7" color="gray" indeterminate />
    </template>
  </v-carousel>
</template>

<script>
export default {
  data() {
    return {
      baseUrl: process.env.VUE_APP_DOMAIN,
      enabled: undefined,
      photos: []
    };
  },
  mounted() {
    this.$axios
      .get(`${process.env.VUE_APP_DOMAIN}/backend/carousel/`)
      .then(
        response => (
          (this.photos = response.data.photos),
          (this.enabled = response.data.enabled)
        )
      );
  }
};
</script>
