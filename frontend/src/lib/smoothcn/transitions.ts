export const sTransitions = {
  spring: {
    gentle: { type: "spring", stiffness: 100, damping: 20 },
    snappy: { type: "spring", stiffness: 300, damping: 30, mass: 1 },
    solid: {
      type: "spring",
      stiffness: 250,
      damping: 30,
      mass: 1.2,
    },
    bouncy: { type: "spring", stiffness: 400, damping: 10 },
    press: { type: "spring", stiffness: 500, damping: 30 },
    hover: { type: "spring", stiffness: 400, damping: 25 },
  },
  ease: {
    standard: [0.4, 0, 0.2, 1],
    inOut: "easeInOut",
  },
} as const;
