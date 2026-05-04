import { sTransitions } from "./transitions";

export const sVariants = {
  fadeIn: {
    initial: { opacity: 0, scale: 0.95 },
    animate: {
      opacity: 1,
      scale: 1,
    },
    exit: { opacity: 0, scale: 0.95 },
    transition: sTransitions.spring.snappy,
  },
  fadeSlideUp: {
    initial: {
      opacity: 0,
      y: 20,
    },
    animate: {
      opacity: 1,
      y: 0,
    },
    exit: {
      opacity: 0,
      y: 20,
    },
    transition: sTransitions.spring.snappy,
  },
  blurIn: {
    initial: { opacity: 0, filter: "blur(10px)" },
    animate: {
      opacity: 1,
      filter: "blur(0px)",
    },
    exit: { opacity: 0, filter: "blur(10px)" },
    transition: sTransitions.spring.gentle,
  },
};
