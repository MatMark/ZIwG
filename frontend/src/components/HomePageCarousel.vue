<template>
  <v-carousel
    v-if="photos"
    cycle
    height="200"
    hide-delimiter-background
    show-arrows-on-hover
  >
    <template v-if="photos">
      <v-carousel-item
        v-for="(photo, key) in photos.data"
        :key="key"
        :src="photo.download_url"
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
      photos: []
    };
  },
  mounted() {
    this.$axios
      .get("https://picsum.photos/v2/list?page=2&limit=3")
      .then(response => (this.photos = response));
  }
};
</script>
