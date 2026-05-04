export const sGestures = {
  bounce: {
    whileHover: { scale: 1.05, y: -2 },
    whilePress: { scale: 0.95, y: 0 },
  },
  press: {
    whileHover: { scale: 1.04 },
    whilePress: { scale: 0.96 },
  },
  lift: {
    whileHover: { y: -4, transition: { duration: 0.2 } },
  },
} as const;
