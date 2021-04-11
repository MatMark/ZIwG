<template>
  <WorkInProgress />
</template>

<script>
import WorkInProgress from "@/views/WorkInProgress.vue";
export default {
  name: "ProductDetails",
  components: {
    WorkInProgress
  },
  data() {
    return {
      product: {}
    };
  }
};
</script>
